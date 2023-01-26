import typing as t
from dataclasses import dataclass


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

    def __repr__(self):
        return f'<{self.__class__.__name__} of kohi>'

    __str__ = __repr__

    @property
    def errors(self):
        return self._errors

    def _handle_errors(self):
        if not self._throw or len(self._errors) < 1:
            return
        
        message = self._errors[0]
        
        if len(self._errors) > 1:
            message = f'{len(self._errors)} errors occurred'
            
        ValidationError = type('ValidationError', (Exception,), {})
        raise ValidationError(message)

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

    def validate(self, data: t.Any):
        """Validate the given data against the schema"""
        self.reset()
        for validator in self._validators:
            error = validator(data, self) # type: ignore
            if error:
                self._errors.append(error)
        self._handle_errors()                
        return len(self.errors) == 0

    def reset(self):
        self._errors = []
    
    def throw(self):
        self._throw = True
        return self

    def label(self, text: str):
        self._label = text
        return self
        