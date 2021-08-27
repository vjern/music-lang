# Music Lang

A draft of a language to ~~program~~ write music ! (and dump it to MIDI format using [mido]())

```c
// starting from a3
c c g g a a g  // whitespace is ignored
f f e e d d c  // can you guess the tune ? 
```

Only the above works for now, future features are listed below.

## How to use

Clone this repo and do

```
python -m midi <my-text-file>
```

to generate a .mid file that you can then read with your favorite media player.

## Notes

Notes are single-letter symbols using their anglo-saxon names (A-G == from la to sol). You can add the exact octave to play:

```c
// a3 is default
a 
// == 
a3
```

If no octave is provided, the interpreter will deduce one from the default note reference (a3 by default).

## Rhythm

Each note has a duration. The default duration is 1, == a **noire**.

Follows that:

* 1/2 une `croche`;
* 1/4 une `double`;
* 2 une `blanche`;


and so on. You can set a specific note's duration with `<note>/<duration>`:

```c
c c g g a a g/2
f f e e d d c/2
```

Add a dot at the end of the duration to eg have a croche pointée:

```c
g/1/2.
```

## Alterations

Simply `<note>_[b#]`:

```c
c_b
c_#
```

## Blocks

Blocks allow you to control default duration & reference frequency as you would scopes:

```c
{
    !/2  // set the default duration to croche for this block
    c c g g
}
```

## Repetitions

```c
a * 3 // repeat notes
{ a a } * 3 // or entire blocks
```

## Loops

```c
loop 35 times {
    c c g g
}
```

## Phrases

Describe and reuse phrases here and there!

```c
theme = {
    !/1
    c c g g a a g/2
    f f e e d d c/2
}

couplet = { g g f f e e d/2 }

theme
couplet
couplet
theme
```

## Plusieurs portées ?

Plusieurs fichiers duh

Ou sinon 

```c
// Portée 1
a a b b
---
// Portée 2
c c d d
```

## Plusieurs voix sur une meme portée ?

Ideas welcome

See more unstructured [ideas](IDEAS.md).
