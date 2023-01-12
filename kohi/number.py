import typing as t
from numbers import Number
from .base import BaseSchema


class NumberSchema(BaseSchema):
    def __init__(self):
        super().__init__((int, float))

    def float(self):
        self.type = float
        return self

    def int(self):
        self.type = int
        return self

    def lt(self, num: t.Type[Number]):
        return self.add_validator(
            'is-lt',
            lambda data: None if data < num else f'number must be less than {num}',
            False
        )

    def gt(self, num: t.Type[Number]):
        return self.add_validator(
            'is-gt',
            lambda data: None if data > num else f'number must be greater than {num}',
            False
        )

    def lte(self, num: t.Type[Number]):
        return self.add_validator(
            'is-lte',
            lambda data: None if data <= num else f'number must be less than or equal to {num}',
            False
        )

    def gte(self, num: t.Type[Number]):
        return self.add_validator(
            'is-gte',
            lambda data: None if data >= num else f'number must be greater than or equal to {num}',
            False
        )

    def min(self, num: t.Type[Number]):
        return self.gte(num)

    def max(self, num: t.Type[Number]):
        return self.lte(num)

    def positive(self):
        return self.gt(0)

    def negative(self):
        return self.lt(0)
