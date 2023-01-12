import typing as t
from dataclasses import dataclass


@dataclass
class Validator:
    name: str
    fn: t.Callable[
        [
            t.Any,
            # t.Type['BaseSchema']
        ],
        t.Optional[str]
    ]

    def __call__(self, data: t.Any):
        return self.fn(data)
    

class BaseSchema:
    def __init__(self, type: t.Union[t.Tuple[t.Callable], t.Callable], type_validator:t.Optional[t.Callable]=None):
        self.type = type
        
        if not type_validator:
            def type_validator(data):
                if not isinstance(data, self.type):
                    if isinstance(self.type, tuple):
                        t_str = ', '.join(map(lambda t: t.__name__, self.type))
                        return f'data type is not of expected types: {t_str}'
                    return f'{data} is not of type {self.type.__name__}'
                    
        self._validators: t.List['Validator'] = [Validator('is-type', type_validator)]
        self._throw: bool = False
        self._errors: t.List[str] = []

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

    def add_validator(self, name: str, fn: t.Callable[[t.Any], t.Optional[str]], exclusive:bool=True):
        if exclusive and any(map(lambda el: el.name == name, self._validators)):
            return
        self._validators.append(Validator(name=name, fn=fn))
        return self

    def validate(self, data: t.Any):
        """Validate the given data against the schema"""
        self.reset()
        for validator in self._validators:
            error = validator(data)
            if error:
                self._errors.append(error)
        self._handle_errors()                
        return len(self.errors) == 0

    def reset(self):
        self._errors = []
    
    def throw(self):
        self._throw = True
        return self
        