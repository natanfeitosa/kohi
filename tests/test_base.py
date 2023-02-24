from kohi.base import BaseSchema
from kohi.exceptions import ValidationError


def test_add_validator():
    b = BaseSchema(list)
    arg = [0, 1, 2, 3]

    assert b.validate(arg)

    def more_than_five(data, schema):
        if len(data) < 6:
            return 'must have more than 5 items'
    b.add_validator('more-than-five', more_than_five)

    assert not b.validate(arg)

def test_label():
    b = BaseSchema(object)

    label = 'object_test'

    assert (not b._label)
    assert b.label(label) == b
    assert b._label == label

def test_custom_messages():
    ob = BaseSchema(tuple)
    
    assert not ob.validate(True)
    assert ob.errors[0] == 'data type is not of expected type(s): tuple'

    message = 'o tipe de {label} deve ser igual um em: {types}'
    ob1 = BaseSchema(tuple, None, message)
    
    assert not ob1.label('object_test').validate(True)
    assert ob1.errors[0] == message.format(label='object_test', types='tuple')

def test_raise():
    b = BaseSchema(tuple).throw()

    try:
        assert b.validate(True)
    except Exception as error:
        if isinstance(error, ValidationError):
            assert True
