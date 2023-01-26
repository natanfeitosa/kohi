from kohi import EnumSchema


def test_base():
    assert EnumSchema().validate(1)
    assert EnumSchema().validate('')
    assert EnumSchema().validate(1.0)

def test_one_of():
    assert EnumSchema().one_of([1]).validate(1)
    assert EnumSchema().one_of([1.0]).validate(1.0)
    assert not EnumSchema().one_of([1.0]).validate('1')

def test_not_one_of():
    assert EnumSchema().not_one_of([1]).validate('1')
    assert not EnumSchema().not_one_of([1]).validate(1)
    assert not EnumSchema().not_one_of(['1']).validate('1')