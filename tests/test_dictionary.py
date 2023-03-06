from kohi import DictSchema, StringSchema, NumberSchema


def test_base():
    assert not DictSchema().validate(1)
    assert not DictSchema().validate('')
    assert not DictSchema().validate(True)

    d = DictSchema('o parametro não é do tipo dict')

    assert not d.validate(0)
    assert d.errors[0] == 'o parametro não é do tipo dict'

def test_errors_list():
    d = DictSchema().props(
        name=StringSchema().length(4),
        age=NumberSchema().lte(1).default(1)
    )

    assert d.validate({ 'name': 'kohi', 'age': 1 })
    assert not d.validate({ 'name': 'Github', 'age': 15 })
    assert d.throw().validate({ 'name': 'Gitlab' })
