from mlang import core


def tokenize(*a):
    return list(core.tokenize(*a))


def test_basic():
    text = 'a b c _'
    assert tokenize(text) == ['a', 'b', 'c', '_']


def test_exact_notes():
    text = 'a3 b4'
    assert tokenize(text) == ['a3', 'b4']


def test_comments():
    text = '// b a'
    assert tokenize(text) == []


def test_comments_inline():
    text = 'a b // b'
    assert tokenize(text) == ['a', 'b']


def test_duration():
    text = 'a/3'
    assert tokenize(text) == ['a', '/', '3']


def test_blocks():
    text = 'a { a b3 c }'
    assert tokenize(text) == ['a', '{', 'a', 'b3', 'c', '}']


def test_imperative():
    text = '!a3 a b'
    assert tokenize(text) == ['!', 'a3', 'a', 'b']


def test_repeat():
    text = 'a * 3 b { b } * 2'
    assert tokenize(text) == ['a', '*', '3', 'b', '{', 'b', '}', '*', '2']
