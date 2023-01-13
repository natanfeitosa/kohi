
# kohi

<p align="center">A powerfull schema validator</p>

![GitHub Repo stars](https://img.shields.io/github/stars/natanfeitosa/kohi)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/natanfeitosa/kohi/pytest.yml?label=Pytest&logo=github)
![GitHub](https://img.shields.io/github/license/natanfeitosa/kohi)

## Quickstart

To validate a type you can import your schema validator from `kohi` or `from kohi.<type> import <type>Schema`

e.g.

Let's check if a person's date of birth is a positive integer less than the current date — 2023 — and greater than or equal to 2005

```python
from kohi import NumberSchema
# from kohi.number import NumberSchema

n = NumberSchema().int().positive().lt(2023).gte(2005)

print(n.validate(2005)) # True
print(n.validate(2022)) # True
print(n.validate(2004)) # False
print(n.validate(2023)) # False

# You can see the errors generated in the last `validate` call just by accessing the `errors` property
# print(n.errors) # ['number must be less than 2022']
```

## Validators

* [`kohi.base.BaseSchema`](#baseschema)
> Only one base class for all schema validators
* [`kohi.number.NumberSchema`](#numberschema)
> or `kohi.NumberSchema`
* [`kohi.string.StringSchema`](#stringschema)
> or `kohi.StringSchema`

## Methods

### `BaseSchema`
* `add_validator(name, func): Self`
  > Add a custom data validator
* `validate(data): bool`
  > The method to be called when we validate the schema
* `reset(): None`
  > Reset error list
* `throw(): Self`
  > By default no errors are thrown, but when this method is chained a `ValidationError` will be thrown

### `NumberSchema`
inherits from [`BaseSchema`](#baseschema)
> By default validates int and float 

* `float(): Self`
  > Validate only `float`
* `int(): Self`
  > Validate only `int`
* `lt(num): Self`
  > Validates if the data is less than `num`
* `gt(num): Self`
  > Validates if the data is greater than `num`
* `lte(num): Self`
  > Validates if the data is less than or equal to `num`
* `gte(num): Self`
  > Validates if the data is greater than or equal to `num`
* `min(num): Self`
  > Just an alias for `gte(num)`
* `max(num): Self`
  > Just an alias for `lte(nun)`
* `positive(): Self`
  > Just an alias for `gt(0)`
* `negative(): Self`
  > Just an alias for `lt(0)`

### StringSchema
inherits from [`BaseSchema`](#baseschema)

## Dev env

* install development dependencies
* check types using `mypy`
* run all tests using `pytest`
