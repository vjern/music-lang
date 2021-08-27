## Message

\<note>[/<durée>]

## Setter

Starts with `!`

```c
!<note> // Set the default reference note
!<durée> // Set the default duration
```

## Notes

soit les noms germaniques (a-h)
soit les noms français (do-si)

par défaut `a3`

un vrai nom de note:

```
a3
b4
a b c d e f g [h]
do re mi fa sol la si
```

et le programme devrait deviner quelle note jouer d'après la dernière en date si aucune octave fournie

### Altérations

```
a_b
a_bb
a_#
a_##
```

## Durées

par défaut 1 (noire)

1 noire

puis des subdivisions:

1/2 croche
1/4 double

etc

.2, .4 for shorthand

## Repetitions

```c
<note> * 2
{ <note> <note> } * 2
```

## Boucles

```c
loop X { // repeat X times

}
```

## "Functions" == Phrases

```c
phrase phraseName {

}

// eg

phrase mainTheme {
    !a3 !.2 // those are local to the function / loop / block
    a a
    b b
}

```

## Mesures

Maybe we could enforce the writing of separate "mesures" as in:

```c
chiffrage 4/4
chiffrage C

// One line == one mesure

{ a a b b }
{ !*2 b+ b- }

chiffrage 6/4

```

## Armure

```c
armure 3b // 3 bemols (b e a)
armure 3# // 3 dièses (f c g)
// or
ton c maj // do majeur
ton c // default to maj
ton c flat // == maj
ton c moll // == min
```

## Accords, Arpèges

Renversements

```
ton c maj
[I III V I]
[VII]
```

## Grammar


```c#
lex {
    SET_OP = "!"
    REP_OP = "*"
    SLASH_OP = "/"
    DOT_OP = "."
    ONE_LITERAL = "1"
    NUMBER_LITERAL = "\d+"
    NOTE_NAME = "[a-e]|do|re|ré|mi|fa|sol|la|si"
}

PROG = INSTRUCTION*

INSTRUCTION =
| EXPR
| LOOP
| PHRASE

EXPR =
| SETTER
| BLOCK
| NOTE
| NOTE SLASH_OP DURATION
| EXPR REP_OP NUMBER_LITERAL

SETTER = SET_OP SET_CLAUSE

SET_CLAUSE =
| REP_OP NUMBER_LITERAL
| DURATION
| NOTE

DURATION =
| NUMBER_LITERAL
| ONE_LITERAL ~ SLASH_OP ~ NUMBER_LITERAL
| DOT_OP ~ NUMBER_LITERAL

NOTE =
| NOTE_NAME
| NOTE_NAME ~ NUMBER_LITERAL
| NOTE ~ UNDERSCORE_OP ~ b
| NOTE ~ UNDERSCORE_OP ~ #
```

## Transposition

```
phrase = { a b | b c }
phrase = transpose phrase +
```

## Marches harmoniques

## Complexes / Rythmes custom

```c
// Triolet sur noire

// Or lets try to create the imperial march!
// Un sixtolet avec une croche pointée et 3 double croches
// En ternaire (12/8)
!1. // rythme par défaut = noire pointée
!a3
a
a/.2.  // Peut etre que le point pourrait s'activer par défaut ? mauvaise idée en fait
-/.4. * 3  // - pour meme note ?
-/.2.
-/.4. * 3
-/.4. * 3
-/.2.

// How can we make this into a reusable rythm ?
// make it a phrase and transpose it maybe

rolling = { a { a/.2. a/.4 * 3 } * 2 a/.4 * 3 a/.2 }

// play <var> <transposition info> (will be appended beforehand)
play rolling + // Play it an octave higher
play rolling 2 // Play it 2 half-tons higher
play rolling 4 // Play it 2 tons higher

play rolling +
// can be shortened to
$(rolling +)
```

## Better rhythm notations

Blanches et rondes seront moins fréquentes que croches, donc peut être pourrait-on inverser leurs notations ?

initialement

```c
a/2 // blanche
a/.2 // croche 
```

Plus court encore, on pourrait juste accepter un slash (ou deux) vide pour prendre la moitié :

```c
a/ == a/2
a// == a/4
```