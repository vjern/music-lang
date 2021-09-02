import re
from dataclasses import dataclass, field
from typing import Dict


@dataclass
class LexicalUnit:
    text: str


class Literal(LexicalUnit):
    pass


class NoteLiteral(Literal):
    pass


class DurationLiteral(Literal):
    pass


class Lexifier:
    patterns: Dict[str, str] = field(default_factory=dict)
    def lex(self, token: str) -> LexicalUnit:
        for pat, cls in self.patterns.items():
            if re.match(pat, token):
                return 


# class MlangLexifier(Lexifier):
#     # Note: 