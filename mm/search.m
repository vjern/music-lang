// 2 => blanche
// 3 => blanche pointée 
// 1 => noire
// /2 => croche
// /4 => double
// etc
// pointée => X.
// noire pointée => 3 ou 1/2.
// _ => silence
// <note>/<durée pour cette note uniquement>
// !<note> note de départ
// !<durée> durée par défaut
// + Monter d'une octave, - Descendre d'une octave

// altérations ?

// a3_b, a3_#

// accords / arpèges ?

// boucles ?
// ( a b ) *2

// plusieurs voix ?
// [ 
//    a b b
//    c c c 
// ]

!a3
!.2
!*4

a a // == 2 fois 4 croches of a3
a *2

// nested loops
loop 20
    loop 10
        a *4
