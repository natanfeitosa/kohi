import re, uuid
import typing as t
from .base import BaseSchema

__all__ = ('StringSchema',)


class StringSchema(BaseSchema):
    def __init__(self, message: t.Optional[str] = None):
        super().__init__((str,), message=message)

    def min(self, min_length: int, message: t.Optional[str] = None):
        def validator(data, schema):
            label = schema._label

            if not label:
                label = 'data'

            nonlocal message
            if not message:
                message = '{label} length must be greater than or equal to {length}'
                
            if len(data) < min_length:
                return message.format(length=min_length, label=label)
                
        return self.add_validator('min-length', validator)
    
    def length(self, length: int, message: t.Optional[str] = None):
        def validator(data, schema):
            label = schema._label

            if not label:
                label = 'data'

            nonlocal message
            if not message:
                message = '{label} length must be equal to {length}'
                
            if len(data) != length:
                return message.format(length=length, label=label)
                
        return self.add_validator('length', validator)

    def max(self, max_length: int, message: t.Optional[str] = None):
        def validator(data, schema):
            label = schema._label

            if not label:
                label = 'data'

            nonlocal message
            if not message:
                message = '{label} length must be less than or equal to {length}'
                
            if len(data) > max_length:
                return message.format(length=max_length, label=label)
                
        return self.add_validator('max-length', validator)
    
    def url(self, message: t.Optional[str] = None):
        def validator(data, schema):
            label = schema._label

            if not label:
                label = 'data'

            nonlocal message
            if not message:
                message = '{label} is not a valid URL'
                
            regex = re.compile(
                r'^(?:http|ftp)s?://'  # http:// or https://
                r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
                r'localhost|'  # localhost...
                r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
                r'(?::\d+)?'  # optional port
                r'(?:/?|[/?]\S+)$', re.IGNORECASE)
            
            if not regex.match(data):
                return message.format(label=label)
                
        return self.add_validator('is-url', validator)

    def uuid(self, message: t.Optional[str] = None):
        def validator(data, schema):
            label = schema._label

            if not label:
                label = 'data'

            nonlocal message
            if not message:
                message = '{label} is not a valid UUID'
                
            try:
                uuid.UUID(data)
            except ValueError:
                return message.format(label=label)
        return self.add_validator('is-uuid', validator)

    def starts_with(self, text: str, message: t.Optional[str] = None):
        def validator(data, schema):
            label = schema._label

            if not label:
                label = 'data'

            nonlocal message
            if not message:
                message = '{label} must starts with {text}'
                
            if not data.startswith(text):
                return message.format(text=text, label=label)
                
        return self.add_validator('starts-with', validator)

    def ends_with(self, text: str, message: t.Optional[str] = None):
        def validator(data, schema):
            label = schema._label

            if not label:
                label = 'data'

            nonlocal message
            if not message:
                message = '{label} must end with {text}'
                
            if not data.endswith(text):
                return message.format(text=text, label=label)
                
        return self.add_validator('ends-with', validator)

    # def email(self):
    #     ...
