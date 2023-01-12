import re, uuid
from .base import BaseSchema

__all__ = ('String',)


class StringSchema(BaseSchema):
    def __init__(self):
        super().__init__((str,))

    def min(self, min_length: int):
        return self.add_validator(
            'min-length',
            lambda data: None if len(data) >= min_length else f'data length must be greater than or equal to {min_length}'
        )
    
    def length(self, length: int):
        return self.add_validator(
            'length',
            lambda data: None if len(data) == length else f'data length must be equal to {length}'
        )

    def max(self, max_length: int):
        return self.add_validator(
            'max-length',
            lambda data: None if len(data) <= max_length else f'data length must be less than or equal to {max_length}'
        )
    
    def url(self):
        def test(data):
            regex = re.compile(
                r'^(?:http|ftp)s?://'  # http:// or https://
                r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
                r'localhost|'  # localhost...
                r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
                r'(?::\d+)?'  # optional port
                r'(?:/?|[/?]\S+)$', re.IGNORECASE)
            
            if not regex.match(data):
                return 'string is not a valid URL'
        return self.add_validator('is-url', test)

    def uuid(self):
        def test(data):
            try:
                uuid.UUID(data)
            except ValueError:
                return 'string is not a valid UUID'
        return self.add_validator('is-uuid', test)

    def starts_with(self, text: str):
        return self.add_validator('starts-with', lambda data: None if data.startswith(text) else f'string must starts with {text}')

    def ends_with(self, text: str):
        return self.add_validator('ends-with', lambda data: None if data.endswith(text) else f'string must end with {text}')

    # def email(self):
    #     ...
