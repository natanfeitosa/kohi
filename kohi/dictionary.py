import typing as t
from .base import BaseSchema


__all__ = ('DictSchema',)


class DictSchema(BaseSchema):
    def __init__(self, message: t.Optional[str] = None):
        super().__init__((dict,), message=message)
        self._props: dict = {}

    def props(self, **props):
        self._props = props
        return self

    def _prepare_new_label(self, key: str):
        if self._label:
            return f'{self._label}.{key}'
        return key

    def _validate_props(self):
        for key, schema in self._props.items():
            if not isinstance(schema, BaseSchema):
                raise TypeError(f'The validator at {key} is not a valid schema validator')

            def validator(data, parent):
                nonlocal schema, key
                validate = schema.label(parent._prepare_new_label(key))

                _data = None
                if key in data:
                    _data = data[key]

                if not validate.validate(_data):
                    new_errors = [*parent.errors, *validate.errors]
                    parent._errors = new_errors

            self.add_validator(f'valide-{key}', validator)

    def _validate(self, data: t.Any, checks=True):
        self._validate_props()
        return super()._validate(data, checks)