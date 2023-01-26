import typing as t
from .base import BaseSchema

__all__ = ('EnumSchema',)


class EnumSchema(BaseSchema):
    def __init__(self, message: t.Optional[str] = None):
        super().__init__((object,), message=message) #type: ignore

    def one_of(self, opts: t.Iterable, message: t.Optional[str] = None):
        def validator(data, schema):
            label = schema._label

            if not label:
                label = 'data'

            nonlocal message
            if not message:
                message = '{label} is not a valid value'

            if not data in opts:
                return message.format(label=label, value=data, options=opts)
                
        return self.add_validator('one-of', validator)

    def not_one_of(self, opts: t.Iterable, message: t.Optional[str] = None):
        def validator(data, schema):
            label = schema._label

            if not label:
                label = 'data'

            nonlocal message
            if not message:
                message = '{label} is not a valid value'

            if data in opts:
                return message.format(label=label, value=data, options=opts)
                
        return self.add_validator('not_one_of', validator)
