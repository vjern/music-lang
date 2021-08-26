## Message

\<note>[/<durée>]

## Setter

Starts with `!`

```
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
do re ré mi fa sol la si
```

et le programme devrait deviner quelle note jouer d'après la dernière en date si aucune octave fournie

### Altérations

```
a_b
a_#
```

## Durées

par défaut 1 (noire)

1 noire

puis des subdivisions:

1/2 croche
1/4 double

etc

.2, .4 for shorthand

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
a&[V/I]
```

## Marches harmoniques