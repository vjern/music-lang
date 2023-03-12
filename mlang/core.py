import re
from typing import List
from dataclasses import dataclass

import toksic


def tokenize(text: str):

    for i, row in enumerate(text.split('\n')):

        if not row.strip() or row.strip().startswith('//'):
            continue

        tokens = toksic.tokenize(row, toksic.Trie().init(['//', '=>']))
        tokens = list(toksic.split(tokens, '//'))[0]
        print(tokens)

        for token in tokens:
            token.lineno = i

        yield from tokens


@dataclass
class Note:
    name: str


class Notes:
    A3 = 69
    A0 = 33
    @classmethod
    def make(cls, name: str, h: int):
        return cls.A0 + dodeca(name) + h * 12


def dodeca(name: str) -> int:
    return 'aabccddeffg'.index(name)


def get_freq(name: str, ref: int = Notes.A3) -> int:
    m = re.match(r'^([a-zA-Z]{,2})(\d)?$', name)
    if m is None:
        raise ValueError(f'Invalid note name {name!r}')
    name, h = m.groups()
    name = dict(zip(['do', 're', 'mi', 'fa', 'sol', 'la', 'si'], 'abcdefg')).get(name, name)
    print(f'{name = } {h = }')
    if h is not None:
        return Notes.make(name, int(h))
    # suggestion goes like this
    # a sliding window of 7
    # a b c d e f g
    # when starting on a, bcd is ^ and efg is v
    default_h = (ref - Notes.A0) // 12
    default_note = 'aabccddeffg'[(ref - Notes.A0) % 12]
    # TODO: smart suggestion as commented above
    return Notes.make(name, default_h)


@dataclass
class Sound:
    freq: int = 57
    duration: int = 1
    @classmethod
    def forNote(cls, note: Note):
        return cls(get_freq(note.name))


@dataclass
class Track:
    units: List[Note]
    def to_midi(self, bpm: int = 120):
        for unit in self.units:
            unit = Sound.forNote(unit)
            step = int(unit.duration * 1000 * (60 / bpm))
            msg = {
                'type': 'note_on',
                'note': unit.freq,
                'velocity': 64,
                'time': 0
            }
            yield msg
            yield {**msg, 'type': 'note_off', 'time': step}


def lex(token: str):
    # return Sound()
    return Note(token)


def parse(text: str):
    tokens = tokenize(text)
    track = []

    for token in  tokens:
        track.append(lex(token))

    return Track(track)


def compile(text: str):
    tokens = tokenize(text)
    track = []
    for token in  tokens:
        track.append(lex(token))

    track = Track(track)

    data = [
        {
            'track': 1,
            'note': note.name,
            'duration': '1',
            'n': 1
        }
        for note in track.units
    ]

    return data
