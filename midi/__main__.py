import sys
import mido

from .core import parse

if __name__ == '__main__':

    filepath = sys.argv[1:] and sys.argv[1]
    if not filepath:
        exit(1)
    
    with open(filepath) as f:
        track = parse(f.read())
    
    midi = mido.MidiFile()
    midi_track = mido.MidiTrack()
    midi.tracks.append(midi_track)

    midi_track.append(mido.Message('program_change', program=1, time=0))

    for message in track.to_midi():
        print(message)
        midi_track.append(mido.Message(**message))
    
    midi.save(filepath + '.mid')
    print(f'Saved to {filepath}.mid')