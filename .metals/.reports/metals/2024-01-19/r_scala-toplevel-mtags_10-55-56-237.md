error id: file:///D:/code/KdP/11ueb/aufgabe1.scala:[1396..1397) in Input.VirtualFile("file:///D:/code/KdP/11ueb/aufgabe1.scala", "/* 
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
    def 
}")
file:///D:/code/KdP/11ueb/aufgabe1.scala
file:///D:/code/KdP/11ueb/aufgabe1.scala:44: error: expected identifier; obtained rbrace
}
^
#### Short summary: 

expected identifier; obtained rbrace