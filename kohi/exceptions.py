import typing as t


__all__ = ('ValidationError', 'ParseError')


class ValidationError(Exception):
    def __init__(self, errors: t.List[str]):
        self.errors = errors
        message = errors[0]

        if (len_errors := len(errors)) > 1:
            message = f'{len_errors} errors occurred'

        super().__init__(message)

class ParseError(Exception):
    """error thrown when something goes wrong in the `parse()` method"""
