from kohi.base import BaseSchema

def test_add_validator():
    b = BaseSchema(list)
    arg = [0, 1, 2, 3]

    assert b.validate(arg)

    def more_than_five(data):
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