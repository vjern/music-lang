from mlang.core import lex


class Symbols(lex.Enum):
    pass

# class TestNote:

#     def test_basic(self):
#         assert lex.lex(['a']) == [lex.Note(name='a')]
#         assert lex.lex(['A']) == [lex.Note(name='A')]

#     def test_freq(self):
#         assert lex.lex(['a3', 'b4']) == [lex.Note(name='a', octave=3)]


# class TestDuration:

#     def test_basic(self):
#         assert lex.lex(['1']) == [lex.Duration('1')]
#         assert lex.lex(['1.']) == [lex.Duration('1.')]
#         assert lex.lex(['1/2']) == [lex.Duration('1/2')]
#         assert lex.lex(['1/2.']) == [lex.Duration('1/2.')]
