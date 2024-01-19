file:///D:/code/KdP/11ueb/aufgabe1.scala
### dotty.tools.dotc.core.TypeError$$anon$1: Toplevel definition <error> is defined in
  D:/code/KdP/11ueb/aufgabe1.scala
and also in
  D:/code/KdP/11ueb/aufgabe1.scala
One of these files should be removed from the classpath.

occurred in the presentation compiler.

action parameters:
offset: 1391
uri: file:///D:/code/KdP/11ueb/aufgabe1.scala
text:
```scala
/* 
 * Uebungsblatt 11
 * Author: Julian Mueller, David Glaser
 * due date: 2024-01-19
 */

// Aufgabe 1a
// In Scala wird Wertesemantik bei der Zuweisungen von primitive Datentypen und Referenzsemantik bei der Zuweisung von complexen Datentypen verwendet.
// Bei Wertesemantik wird der Wert kopiert und bei Referenzsemantik wird die Referenz kopiert.

// Beispiel:
// Wertesemantik
// var a = 1
// var b = a
// a = 2
// println(b) // 1

// Referenzsemantik
// var a = Array(1,2,3)
// var b = a
// a(0) = 4
// println(b(0)) // 4

// Aufgabe 1b
// Man erstellt b als Referenz auf a und c als Kopie von a.
// c(2) = a(1) -> Hier wird das 3 Array von c auf das 2 Array von a gesetzt.
// c(2)(1) = 6 -> Hier wird das 2 Element des 3 Array von c auf 6 gesetzt und da c(2) auf a(1) zeigt wird das 2 Element des 2 Array von a auf 6 gesetzt, sowie in b.
// b(2)(2) = 7 -> Hier wird das 3 Element des 3 Array von b auf 7 gesetzt und da b(2) auf a(2) zeigt wird das 3 Element des 3 Array von a auf 7 gesetzt, aber nicht in c.
// Das sind die Arrays nach den Aenderungen:
// a: [[2, 4, 6, 8], [1, 6, 3], [3, 4, 7]]
// b: [[2, 4, 6, 8], [1, 6, 3], [3, 4, 7]]
// c: [[2, 4, 6, 8], [1, 2, 3], [1, 6, 3]]

// (a(1) == c(1)) -> true 
// (b(2) == c(2)) -> false
// (a == c) -> false
// b(2)(2) -> 7
// c(1)(1) -> 2
// c(2)(2) -> 3

// Aufgabe 1c
class Geom3D {
    d@@
}
```



#### Error stacktrace:

```

```
#### Short summary: 

dotty.tools.dotc.core.TypeError$$anon$1: Toplevel definition <error> is defined in
  D:/code/KdP/11ueb/aufgabe1.scala
and also in
  D:/code/KdP/11ueb/aufgabe1.scala
One of these files should be removed from the classpath.