from mido import Message, MidiFile, MidiTrack

mid = MidiFile()
track = MidiTrack()
# http://multimedia.uqam.ca/audio/docu/MIDI_JDSPG.pdf

# program => 0 to 127
for i in range(128):
    track.append(Message(type='program_change', program=i, time=50*i + 0))
    track.append(Message('note_on', note=64, velocity=64, time=50*i))
    track.append(Message('note_off', note=64, velocity=64, time=50*i+50))
mid.tracks.append(track)

track = MidiTrack()
track.append(Message('program_change', program=53, time=0))
track.append(Message('note_on', note=43, velocity=64, time=0))
track.append(Message('note_off', note=0, velocity=64, time=50*128))
mid.tracks.append(track)


mid.save('new_song.mid')


# t = Track()

# score = [ A ]

