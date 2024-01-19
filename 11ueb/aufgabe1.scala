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
abstract class Geom3D {
    def volume: Double
    def surfaceArea: Double
}

class Wuerfel(val seitenlaenge: Double) extends Geom3D {
    override def volume: Double = seitenlaenge * seitenlaenge * seitenlaenge
    override def surfaceArea: Double = seitenlaenge * seitenlaenge * 6
}

class Quader(val laenge: Double, val breite: Double, val hoehe: Double) extends Geom3D {
    override def volume: Double = laenge * breite * hoehe
    override def surfaceArea: Double = (laenge * breite + laenge * hoehe + breite * hoehe) * 2
}

class Kugel(val radius: Double) extends Geom3D {
    override def volume: Double = 4.0 / 3.0 * Math.PI * Math.pow(radius, 3)
    override def surfaceArea: Double = 4 * Math.PI * Math.pow(radius, 2)
}

class Tetraeder(val seitenlaenge: Double) extends Geom3D {
    override def volume: Double = Math.pow(seitenlaenge, 3) / (6 * Math.sqrt(2))
    override def surfaceArea: Double = Math.sqrt(3) * Math.pow(seitenlaenge, 2)
}


object Geom3Demo {
  def calculateTotalVolumeAndSurface(geoms: Array[Geom3D]): (Double, Double) = {
    geoms.foldLeft((0.0, 0.0)) { (acc, geom) =>
      (acc._1 + geom.volume, acc._2 + geom.surfaceArea)
    }
  }

  def main(args: Array[String]): Unit = {
    val geometries = Array(
      new Wuerfel(2),
      new Quader(2, 3, 4),
      new Kugel(1),
      new Tetraeder(3)
    )

    val (totalVolume, totalSurface) = calculateTotalVolumeAndSurface(geometries)
  }
}

// Aufgabe 1d

//     +-----------+
//     |   Place   |
//     +-----------+
//     | printMe() |
//     +-----------+
//           ^
//           |
//           |
//     +-----------+
//     |   Region  |
//     +-----------+
//     | printMe() |
//     +-----------+
//           ^
//           |
//           |
//     +-----------+
//     |   State   |
//     +-----------+
//     | printMe() |
//     +-----------+
//           ^
//           |
//           |
//     +-----------+
//     | Maryland  |
//     +-----------+
//     | printMe() |
//     +-----------+


// Die Ausgabe ist:
// Read it.
// Ship it.
// Buy it.
// Read it.
// Box it.

// md.printMe() gibt "Read it." aus, da md vom Typ Maryland ist.
// mid.printMe() gibt "Ship it." aus, da mid vom Typ State ist.
// obj.asInstanceOf[Place].printMe() gibt "Buy it." aus, da obj ursprünglich vom Typ Place ist.
// Nach obj = md gibt obj.asInstanceOf[Maryland].printMe() "Read it." aus, da obj jetzt auf ein Objekt vom Typ Maryland zeigt.
// Nach obj = usa gibt obj.asInstanceOf[Place].printMe() "Box it." aus, da obj jetzt auf ein Objekt vom Typ Region zeigt, das eine Unterklasse von Place ist.