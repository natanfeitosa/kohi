import typing as t
from numbers import Number
from .base import BaseSchema

__all__ = ('NumberSchema',)

class NumberSchema(BaseSchema):
    def __init__(self, message: t.Optional[str] = None):
        super().__init__((int, float), message=message) #type: ignore

    def float(self):
        self._type = float
        return self

    def int(self):
        self._type = int
        return self

    def lt(self, num: t.Type[Number], message: t.Optional[str] = None):
        def validator(data, schema):
            label = schema._label

            if not label:
                label = 'data'

            nonlocal message
            if not message:
                message = '{label} must be less than {num}'

            if not data < num:
                return message.format(label=label, num=num)
                
        return self.add_validator('is-lt', validator, False)

    def gt(self, num: t.Type[Number], message: t.Optional[str] = None):
        def validator(data, schema):
            label = schema._label

            if not label:
                label = 'data'

            nonlocal message
            if not message:
                message = '{label} must be greater than {num}'

            if not data > num:
                return message.format(label=label, num=num)
                
        return self.add_validator('is-gt', validator, False)

    def lte(self, num: t.Type[Number], message: t.Optional[str] = None):
        def validator(data, schema):
            label = schema._label

            if not label:
                label = 'data'

            nonlocal message
            if not message:
                message = '{label} must be less than or equal to {num}'

            if not data <= num:
                return message.format(label=label, num=num)
                
        return self.add_validator('is-lte', validator, False)

    def gte(self, num: t.Type[Number], message: t.Optional[str] = None):
        def validator(data, schema):
            label = schema._label

            if not label:
                label = 'data'

            nonlocal message
            if not message:
                message = '{label} must be greater than or equal to {num}'

            if not data >= num:
                return message.format(label=label, num=num)
                
        return self.add_validator('is-gte', validator, False)

    def min(self, num: t.Type[Number], message: t.Optional[str] = None):
        return self.gte(num, message)

    def max(self, num: t.Type[Number], message: t.Optional[str] = None):
        return self.lte(num, message)

    def positive(self, message: t.Optional[str] = None):
        return self.gt(0, message) #type: ignore

    def negative(self, message: t.Optional[str] = None):
        return self.lt(0, message) #type: ignore

    def nonpositive(self, message: t.Optional[str] = None):
        return self.lte(0, message) #type: ignore

    def nonnegative(self, message: t.Optional[str] = None):
        return self.gte(0, message) #type: ignore
