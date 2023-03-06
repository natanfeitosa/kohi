# kohi

<p align="center">A powerfull schema validator</p>

![GitHub Repo stars](https://img.shields.io/github/stars/natanfeitosa/kohi)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/natanfeitosa/kohi/pytest.yml?label=Pytest&logo=github)
![GitHub](https://img.shields.io/github/license/natanfeitosa/kohi)
![PyPI - Format](https://img.shields.io/pypi/format/kohi)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/kohi)
![PyPI - Package Version](https://img.shields.io/pypi/v/kohi)
![PyPI - Downloads](https://img.shields.io/pypi/dm/kohi)
[![Open Source Helpers](https://www.codetriage.com/natanfeitosa/kohi/badges/users.svg)](https://www.codetriage.com/natanfeitosa/kohi)

## Instalation

Via Poetry:
```sh
poetry add kohi
```

Via PIP:
```sh
pip install kohi
```

Via GitHub (recommended only in dev env):
```sh
git clone https://github.com/natanfeitosa/kohi.git && cd kohi && pip install .
```

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
* [`kohi.enum.EnumSchema`](#enumschema)
> or `kohi.EnumSchema`
* [`kohi.dictionary.DictSchema`](#dictschema)
> or `kohi.DictSchema`

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
* `add_mutation(): Self`
  > Add a mutation function than will run after the `validate` method. P.S. Will only be executed in the `parse` method
* `parse(data): typeof data`
  > Run the `validate` method, the mutations and return a deep clone of data
* `default(data): Self`
  > Set a default value for when the validator receives None and you don't want to generate an error
* `optional(): Self`
  > Allow values None
* `required(error_message=None): Self`
  > Mark the schema as required. Does not allow values None

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
* `nonpositive(): Self`
  > Just an alias for `lte(0)`
* `nonnegative(): Self`
  > Just an alias for `gte(0)`

### StringSchema
inherits from [`BaseSchema`](#baseschema)

* `min(min_length): Self`
  > Validate if the data len is greater than or equal to min_length
* `length(length): Self`
  > Validate if the data len equal to length
* `max(max_length): Self`
  > Validate if the data len is less than or equal to max_length
* `url(): Self`
  > Validate if the data is an url
* `uuid(): Self`
  > Validate if the data is a valid uuid
* `starts_with(text): Self`
  > Validate if the data starts with text
* `ends_with(text): Self`
  > Validate if the data ends with text

### EnumSchema
inherits from [`BaseSchema`](#baseschema)

* `one_of(opts): Self`
  > Validate if the data is in opts
* `not_one_of(opts): Self`
  > Validate that data is different from the values in opts

### DictSchema
inherits from [`BaseSchema`](#baseschema)

* `props(**props): Self`
  > Defines the structure of the dictionary in the format `[key]: ClassValidator`

## Dev env

* install development dependencies
* check types using `mypy`
* run all tests using `pytest`
