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

                if not validate.validate(getattr(data, key, None)):
                    new_errors = [*parent.errors, *validate.errors]
                    print(new_errors)
                    parent._errors = new_errors

            self.add_validator(f'valide-{key}', validator)

    def validate(self, data: t.Any):
        """Validate the given data against the schema"""
        self.reset()
        self._validate_props()
        for validator in self._validators:
            error = validator(data, self) # type: ignore
            if error:
                self._errors.append(error)
        print('len:', len(self.errors))
        self._handle_errors()                
        return len(self.errors) == 0