from typing import List, Dict


def parse():
    pass


class Expr:
    tstr: str


class Clause:
    forms: List[Expr]
    name: str


class Grammar:
    clauses: List[Clause]
    lexes: Dict[str, str]


def test_parse_grammar():

    assert parse_clause("A = B ADD C") == Clause(
        name='A',
        forms=[
            Expr('B ADD C')
        ]
    )

    assert parse_grammar("lex  A = B ADD C")

    text = "3 + 2"

    assert interpret(grammar)