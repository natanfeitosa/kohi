import copy
import typing as t
from functools import reduce
from dataclasses import dataclass
from .exceptions import ValidationError, ParseError

__all__ = ('Validator', 'BaseSchema')

@dataclass
class Validator:
    name: str
    fn: t.Callable[
        [
            t.Any,
            t.Type['BaseSchema']
        ],
        t.Optional[str]
    ]

    def __call__(self, data: t.Any, schema: t.Type['BaseSchema']):
        return self.fn(data, schema)
        
def def_type_validator(message):
    def wrap(data, schema):
        if not isinstance(data, schema._type):
            types = schema._type
            label = schema._label
            
            if not isinstance(types, tuple):
                types = (types,)

            if not label:
                label = 'data'

            nonlocal message
            if not message:
                message = '{label} type is not of expected type(s): {types}'
            
            t_str = ', '.join(map(lambda t: t.__name__, types))
            return message.format(label=label, types=t_str)
    return wrap

class BaseSchema:
    def __init__(
        self,
        type: t.Union[t.Tuple[t.Callable], t.Callable],
        type_validator: t.Optional[t.Callable[[t.Any, t.Type['BaseSchema']], t.Optional[str]]] = None,
        message: t.Optional[str] = None
    ):
        if not type_validator:
            type_validator = def_type_validator(message)
            
        self._type = type
        self._validators: t.List['Validator'] = [Validator('is-type', type_validator)]
        self._throw: bool = False
        self._errors: t.List[str] = []
        self._label: str = ''
        self._mutations: t.List[t.Callable[[t.Any], t.Any]] = []

        self._is_required = True
        self._required_error = '{label} is a required field'
        self._default_value = None

    def __repr__(self):
        return f'<{self.__class__.__name__} of kohi>'

    __str__ = __repr__

    @property
    def errors(self):
        return self._errors

    def _handle_errors(self):
        if not self._throw or len(self._errors) < 1:
            return
            
        raise ValidationError(self.errors)

    def add_validator(
        self,
        name: str,
        fn: t.Callable[[t.Any, t.Type['BaseSchema']], t.Optional[str]],
        exclusive: bool = True
    ):
        if exclusive and any(map(lambda el: el.name == name, self._validators)):
            return
        self._validators.append(Validator(name=name, fn=fn))
        return self

    def _run_validators(self, data: t.Any):
        for validator in self._validators:
            error = validator(data, self) # type: ignore
            if error:
                self._errors.append(error)

    def _return_or_default(self, data: t.Any):
        if not data is None:
            return data

        if self._is_required and self._default_value is None:
            error = self._required_error.format(label=self._label)
            self._errors.insert(0, error)
            return

        return copy.deepcopy(self._default_value)

    def _validate(self, data: t.Any, checks=True):
        if checks and (data := self._return_or_default(data)) != None:
            self._run_validators(data)
        self._handle_errors()
        return len(self.errors) == 0

    def validate(self, data: t.Any):
        """Validate the given data against the schema"""
        self.reset()
        return self._validate(data)

    def parse(self, data: t.Any):
        """Analyzes the data and returns after passing the validation step"""
        cloned = copy.deepcopy(self._return_or_default(data))

        if (cloned != data and data == None) or (cloned == data == None and not self._is_required):
            return cloned

        try:
            self.throw()._validate(cloned, False)
        except Exception as e:
            raise ParseError(str(e)) from e

        if self._mutations:
            # compose
            mutation = reduce(lambda a, b: lambda c: a(b(c)), reversed(self._mutations), lambda s: s)
            cloned = mutation(cloned)

        return cloned

    def add_mutation(self, mutation: t.Callable[[t.Any], t.Any]):
        self._mutations.append(mutation)
        return self

    def reset(self):
        self._errors = []
    
    def throw(self):
        self._throw = True
        return self

    def label(self, text: str):
        self._label = text
        return self

    def default(self, data: t.Any):
        self._default_value = data
        return self

    def optional(self):
        self._is_required = False    
        return self

    def required(self, message: str='{label} is a required field'):
        self._is_required = True
        self._required_error = message
        return self
        