from kohi.base import BaseSchema

def test_label():
    b = BaseSchema(object)

    label = 'object_test'
    
    assert b.label(label) == b