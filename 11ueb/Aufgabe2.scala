//Aufgabe 2

//2a
import scala.io.StdIn.readLine
object CorrectNumber extends Exception { }
object Zahlenraten extends App {
  def getRandomNumber():Int = 
    val r = new scala.util.Random
    return r.nextInt(10)

  val searchedNumner = getRandomNumber()
  try {
    while (true) {
    print("Rate die Nummer zwischen 0 - 10 - Deine Eingabe: ")
    val a = readLine()
    if (a.toInt == searchedNumner) throw CorrectNumber
    }
  } catch {
    case CorrectNumber => print("Die Richtige Nummer wurde gefunden!")
  }
}


//2b
class Fahrzeug(private var color: String, private var speed: Int, private var displacement:Int, private var tireSize: Int ):
  def this() = 
    this("noColor", 0, 0, 0)
  def this(color: String, tires: Int) =
    this(color, 0, 0, tires)
  // .... restliche constructors

  def getSpeed: Int = this.speed
  def getColor: String = this.color
  def getTireSize:Int = this.tireSize
  def getDisplacement:Int = this.displacement

  def setSpeed(newSpeed:Int):Unit = 
    this.speed = newSpeed


object Main extends App {
  val one = new Fahrzeug()
  val two = new Fahrzeug()
  val three = new Fahrzeug()
  val four = new Fahrzeug()
  val fifth = new Fahrzeug()

  print("nr5 speed:" ,fifth.getSpeed)
  fifth.setSpeed(100)
  print("nr5 new speed: " ,fifth.getSpeed)
  print("nr1 current speed: ", one.getSpeed)
}

//2c
class Fahrzeug(private var color: String, private var speed: Int, private var displacement:Int, private var tireSize: Int ):
  private var num_plate = Fahrzeug.number_plate
  Fahrzeug.number_plate = Fahrzeug.number_plate +1

  def this() = 
    this("noColor", 0, 0, 0)
  def this(color: String, tires: Int) =
    this(color, 0, 0, tires)
  // .... restliche constructors

  def getSpeed: Int = this.speed
  def getColor: String = this.color
  def getTireSize:Int = this.tireSize
  def getDisplacement:Int = this.displacement
  def getNumPlate:Int = this.num_plate

  def setSpeed(newSpeed:Int):Unit = 
    this.speed = newSpeed

object Fahrzeug:
  private var number_plate: Int = 1000

object Fuhrpark extends App {
  val one = new Fahrzeug()
  val two = new Fahrzeug()
  val three = new Fahrzeug()

  print("one: ", one.getNumPlate)
  print("two: ", two.getNumPlate)
  print("three: ", three.getNumPlate)
}

//2d
class Fahrzeug(private var color: String, private var speed: Int, private var displacement:Int, private var tireSize: Int ):
  def this() = 
    this("noColor", 0, 0, 0)
  def this(color: String, tires: Int) =
    this(color, 0, 0, tires)
  // .... restliche constructors

  def getSpeed: Int = this.speed
  def getColor: String = this.color
  def getTireSize:Int = this.tireSize
  def getDisplacement:Int = this.displacement

  def setSpeed(newSpeed:Int):Unit = 
    this.speed = newSpeed
  def driving():Unit = println("Driving arround without reason")

class Rennwagen(color: String, speed: Int, tires: Int, displacement: Int, private var isRacing: Boolean) extends Fahrzeug(color, speed, displacement, tires):
  def getRacing: Boolean = this.isRacing
  def setRacing(bol: Boolean) = this.isRacing = bol
  override def driving(): Unit = println("Racing arround on tracks")

class Lastwagen(color: String, speed: Int, tires: Int, displacement: Int, private var load: String ) extends Fahrzeug(color, speed, displacement, tires):
  def getLoad: String = this.load
  def setLoad(newLoad:String) = this.load = newLoad

  override def driving(): Unit = println("driving arround to bring all those sweet goods where they are needed")

class Bobbycar(color: String, speed: Int, tires: Int, displacement: Int, private var isTheBestInTown: Boolean) extends Fahrzeug(color, speed, displacement, tires):
  def isBest: Boolean = this.isTheBestInTown
  def setBestInTown() = this.isTheBestInTown = true

  override def driving(): Unit = println("Im Driving arround in my bobbycar.. driving arround cos i can.")

object Fuhrpark extends App {
  //The Static Type here is Fahrzeug the Dynamic is Bobbycar (Can Change over time)
  val one: Fahrzeug = new Bobbycar("white", 0, 0, 0, true)
  //Beispiel Inklusionspolymorphie 
  print(one.isBest) 
  //Dies wird abgebrochen da .isBest() nicht teil von Fahzeug ist sondern Bobbycar.
}
