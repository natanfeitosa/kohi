from kohi import NumberSchema

def test_base():
    n = NumberSchema()

    assert n.validate(1)
    assert n.validate(0.1)
    assert not n.validate('a')

def test_float():
    n = NumberSchema().float()

    assert not n.validate(1)
    assert n.validate(0.1)

def test_int():
    n = NumberSchema().int()

    assert n.validate(1)
    assert not n.validate(0.1)

def test_lt():
    n = NumberSchema().lt(1)

    assert not n.validate(1)
    assert n.validate(0.1)

def test_gt():
    n = NumberSchema().gt(0.1)

    assert n.validate(1)
    assert not n.validate(0.1)

def test_min():
    n = NumberSchema().min(2)

    assert not n.validate(1)
    assert n.validate(2)

def test_max():
    n = NumberSchema().max(1)

    assert n.validate(1)
    assert not n.validate(2)
    
def test_positive():
    n = NumberSchema().positive()

    assert n.validate(1)
    assert not n.validate(-1)

def test_negative():
    n = NumberSchema().negative()

    assert not n.validate(1)
    assert n.validate(-1)
    