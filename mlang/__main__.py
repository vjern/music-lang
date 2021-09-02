import sys
import mido
import logging
from pathlib import Path
import uuid

_here = Path(__file__).parent

from .core import parse
from .midi_to_wav import midi_to_wav


def playground():
    import flask
    app = flask.Flask(__name__,
        template_folder='playground/templates',
        static_folder='playground/static'
    )
    @app.route('/')
    def home():
        return flask.render_template('home.html')
    @app.route('/play', methods=['POST'])
    def play():
        body = flask.request.get_json()
        code = body['code']
        bpm = int(body['bpm'] or 120) 
        track = parse(code)
        print(f'{track = }')
        id = uuid.uuid4().hex
        to_midi(track, _here / f'playground/static/tmp.mid', bpm)
        midi_to_wav(_here / f'playground/static/tmp.mid', _here / f'playground/static/tmp{id}.wav', bpm)
        return {
            'path': '/static/' + f'tmp{id}.wav'
        }
    app.run(port=8080)


def play():
    pass


def to_midi(track, filepath: str, bpm: int = 120):
    midi = mido.MidiFile()
    midi_track = mido.MidiTrack()
    midi.tracks.append(midi_track)

    midi_track.append(mido.Message('program_change', program=1, time=0))

    for message in track.to_midi(bpm=bpm):
        print(message)
        midi_track.append(mido.Message(**message))
    
    midi.save(filepath)
    print(f'Saved to {filepath}')


if __name__ == '__main__':

    filepath = sys.argv[1:] and sys.argv[1]
    if not filepath:
        exit(1)

    if filepath == 'playground':
        playground()
        exit(0)
    
    with open(filepath) as f:
        track = parse(f.read())
    
    to_midi(track, filepath)
