from kohi import StringSchema

def test_base():
    s = StringSchema()
    assert not s.validate(1)
    assert s.validate('test')

def test_min():
    s = StringSchema().min(5)
    assert not s.validate('test')
    assert s.validate(' test ')

def test_length():
    s = StringSchema().length(12)
    assert s.validate('StringSchema')
    assert not s.validate('test')

def test_max():
    s = StringSchema().max(4)
    assert s.validate('test')
    assert not s.validate(' test ')

def test_url():
    s = StringSchema().url()
    assert s.validate('http://python.org/')
    assert not s.validate(' test ')

def test_uuid():
    s = StringSchema().uuid()
    assert s.validate('5445e68f-75ee-43d8-90e2-5dff48e98fbe')
    assert not s.validate(' test ')

def test_starts_with():
    s = StringSchema().starts_with('ko')
    assert s.validate('kohi')
    assert not s.validate(' test ')

def test_ends_with():
    s = StringSchema().ends_with('hi')
    assert s.validate('kohi')
    assert not s.validate(' test ')
    