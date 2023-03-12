import re
from enum import Enum
from dataclasses import dataclass, field
from typing import Dict, Iterable, Optional


@dataclass
class LexicalUnit:
    text: str
    type: Enum


class Lexifier:

    class Symbols(Enum):
        pass

    @classmethod
    def patterns_from_symbols(cls):
        patterns = {}
        assert hasattr(cls, 'Symbols')
        assert issubclass(cls.Symbols, Enum)
        for key, value in vars(cls.Symbols).items():
            if key[0].isidentifier() and key[0] == key[0].upper():
                patterns[value.value] = key
        return patterns

    def __init__(self, patterns = None):
        if patterns is None:
            patterns = self.patterns_from_symbols()
        self.patterns = patterns
        
    def lex(self, token: str) -> Optional[LexicalUnit]:
        for pat, cls in self.patterns.items():
            if re.match('^%s$' % pat, token):
                return LexicalUnit(token, cls)
        return None


class MyLexifier(Lexifier):
    class Symbols(Enum, str):
        IDENT = r'[\w_]+'
        NUMBER_LITERAL = r'[\d./]+'
        LEFT_BRACKET, RIGHT_BRACKET = '{', '}'
        SLASH = '/'
        DOT = '.'
        LEFT_ANGLE_BRACKET, RIGHT_ANGLE_BRACKET = '<', '>'