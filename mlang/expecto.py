import csv


class Duration:
    pass


class Note:
    pass


def read(file):
    r = csv.DictReader(file)
    r = (
        {
            'track': int(u['track']),
            'note': u['note'],
            'duration': u['duration'] if u['duration'] else '1',
            'n': u['n'] or 1,

        }
        for u in r
    )
    return list(r)