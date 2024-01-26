/* 
a) In Scala gibt es keine Mehrfachvererbung. Findet eine mögliche Erklärung,
warum beim Entwurf der Sprache auf diese Möglichkeit verzichtet wurde.
 */

/* 
Bei der Mehrfachvererbung besteht das Problem, dass zB. bei FUnktioninen:
Class C erbet von Class A und B. Class A und B definieren aber zB. die Funktion test123() unterschiedlich. Wenn Class C die
funktion nicht selbst neu definiert und am ende Benutzt wäre nicht klar welche benutzt werden sollte.
Scala hat sich aber die Möglichkeit offengelassen das System der Mehrfachvererbung mit traits umzusetzen.
 */

/*
b) Verwende den ADT Stack, um ein Programm zu schreiben, das gültige Klam-
merausdrücke aus den Klammern
(,),{,},[,]
erkennt. Ein Klammerausdruck ist gültig, wenn es zu jeder öffnenden Klammer
eine zugehörige schließende Klammer vom gleichen Typ, und zu jeder schließen-
den Klammer eine zugehörige öffnende Klammer vom gleichen Typ gibt, und
wenn die Klammern korrekt geschachtelt sind. Gültige Klammerausdrücke:
([{}])(){{()[]}} und ((()))()()(()) und ()()()
Ungültige Klammerausdrücke:
([)] und (() und ())[] und }{
*/

trait MyStack[A]:
  // Objects of an arbitrary but fixed type A are stored in a stack.
  // Precondition: None
  // Result: None
  // Effect: x is now the most recent element in the stack.
  def push(x : A) : Unit
  // Precondition: Stack is not empty.
  // Result: The most recent element is returned.
  // Effect: The most recent element is removed from the stack.
  def pop() : A
  // Precondition: Stack is not empty.
  // Result: The most recent element is returned.
  // Effect: None
  def top : A
  // Precondition: None
  // Effect: None
  // Result: true is returned if and only if the stack has no elements.
  def isEmpty : Boolean
  // Precondition: None
  // Effect: None
  // Result: The number of elements in the stack is returned.
  def size : Int
  //Precodition: Stack is not empty and of Type Klammern
  //Effect:None
  //Result: true is returned if the Stack is a valid Klammerausdruck


enum Klammern:
  case Nothing
  case RundOpen
  case RundClosed
  case EckigOpen
  case EckigClosed
  case GeschweiftOpen
  case GeschweiftClosed
 
class LinkedNodesStack[A] extends MyStack[A]:
  private class Node(val item: A, val next: Node)

  // Header:
  private var topNode : Node = null
  private var _size : Int = 0

  def isEmpty : Boolean = topNode == null
  def size : Int = _size
  def push(x : A) : Unit =
    topNode = Node(x, topNode)
    _size = _size + 1
  def pop() : A =
    if !isEmpty then
      val result: A = topNode.item
        // If the top node was simultaneously the last node
        // in the chain, topNode becomes null.
        topNode = topNode.next
        _size = _size - 1
        result
      else throw Exception("Stack is empty")
  def top : A =
    if !isEmpty then topNode.item
    else throw Exception("Stack is empty")

object Main extends App {
  val newLL = new LinkedNodesStack[Klammern]
  newLL.push(Klammern.GeschweiftClosed)
  newLL.push(Klammern.RundClosed)
  newLL.push(Klammern.EckigClosed)
  newLL.push(Klammern.EckigOpen)
  newLL.push(Klammern.RundOpen)
  newLL.push(Klammern.GeschweiftOpen)

  //Precondition: LinkedNodeStack of type Klammern
  //Effect: The LinkedNodeStack will be empty after evaluation
  //Result: Returns true if the Stack is a valid Klammerexpression

  def evalKlammern(x:LinkedNodesStack[Klammern]):Boolean = 
    var newList:List[Klammern] = List(Klammern.Nothing)
    while(!x.isEmpty) {
      val item = x.pop()
      item match
        case Klammern.Nothing => return false
        case Klammern.RundOpen => newList = List(Klammern.RundOpen) ::: newList
        case Klammern.RundClosed => 
          newList.head match
            case Klammern.RundOpen => newList = newList.drop(1)
            case _ => return false
        case Klammern.EckigOpen => newList = List(Klammern.EckigOpen) ::: newList
        case Klammern.EckigClosed => 
          newList.head match
            case Klammern.EckigOpen => newList = newList.drop(1)
            case _ => return false
        case Klammern.GeschweiftOpen => newList = List(Klammern.GeschweiftOpen) ::: newList
        case Klammern.GeschweiftClosed => 
          newList.head match
            case Klammern.GeschweiftOpen => newList = newList.drop(1)
            case _ => return false
    }
    if newList.length == 1 then
      return true
    else 
      return false
  print(evalKlammern(newLL))
  println("Here comes the first element: ")
  println(newLL.pop())
}

/* 
c) Erweitere den ADT Stack um eine Methode multipush, die es erlaubt mehr als
ein Element auf dem Stack abzulegen. Implementiere diese Methode anschlie-
ßend in den Implementierungen LinkedNodesStack und ArrayStack (Array
statischer Größe).
 */


trait MyStack[A]:
  // Objects of an arbitrary but fixed type A are stored in a stack.
  // Precondition: None
  // Result: None
  // Effect: x is now the most recent element in the stack.
  def push(x : A) : Unit
  //A Non empty List of arbitrary but fixed type A are stored in a stack
  //Precondition: None
  //Result: None
  //Effect: The Elements in the given List are now at the top the stack
  def multiPush(x: List[A]) : Unit
  // Precondition: Stack is not empty.
  // Result: The most recent element is returned.
  // Effect: The most recent element is removed from the stack.
  def pop() : A
  // Precondition: Stack is not empty.
  // Result: The most recent element is returned.
  // Effect: None
  def top : A
  // Precondition: None
  // Effect: None
  // Result: true is returned if and only if the stack has no elements.
  def isEmpty : Boolean
  // Precondition: None
  // Effect: None
  // Result: The number of elements in the stack is returned.
  def size : Int
  //Precodition: Stack is not empty and of Type Klammern
  //Effect:None
  //Result: true is returned if the Stack is a valid Klammerausdruck

 
class LinkedNodesStack[A] extends MyStack[A]:
  private class Node(val item: A, val next: Node)

  // Header:
  private var topNode : Node = null
  private var _size : Int = 0

  def isEmpty : Boolean = topNode == null
  def size : Int = _size
  def push(x : A) : Unit =
    topNode = Node(x, topNode)
    _size = _size + 1
  def multiPush(x: List[A]): Unit = 
    x.foreach( elem => {
      topNode = Node(elem, topNode)
      _size = _size + 1
    })
  def pop() : A =
    if !isEmpty then
      val result: A = topNode.item
        // If the top node was simultaneously the last node
        // in the chain, topNode becomes null.
        topNode = topNode.next
        _size = _size - 1
        result
      else throw Exception("Stack is empty")
  def top : A =
    if !isEmpty then topNode.item
    else throw Exception("Stack is empty")


import scala.reflect.ClassTag

class ArrayStack[A : ClassTag](capacity: Int) extends MyStack[A]:
  // Header:
  private val n : Int = if capacity < 1 then 1 else capacity
  private val array : Array[A] = new Array[A](n)
  private var amount : Int = 0
  
  def push(x : A) : Unit =
    if amount < array.length then
      array(amount) = x
      amount = amount + 1
    else throw new Exception("The stack is full")
  def multiPush(x: List[A]): Unit = 
    x.foreach( elem => push(elem))
  def pop() : A =
    if !isEmpty then
      val result : A = array(amount - 1)
      array(amount - 1) = null.asInstanceOf[A]
      amount = amount - 1
      result
    else throw new Exception("Stack is empty")
  def top : A =
    if !isEmpty then array(amount - 1)
    else throw new Exception("Stack is empty")
  def isEmpty: Boolean = amount == 0
  def size: Int = amount


/* 
d) Ändere die Implementierung des Stapels mit dynamischen Array so, dass das
Array nicht verdoppelt oder halbiert, sondern vervierfacht und geviertelt wird.
(Die Invariante muss angepasst werden.) Testet eure Implementierung und
vergleicht sie mit der ursprünglichen Implementierung.
 */

 trait MyStack[A]:
  // Objects of an arbitrary but fixed type A are stored in a stack.
  // Precondition: None
  // Result: None
  // Effect: x is now the most recent element in the stack.
  def push(x : A) : Unit
  // Precondition: Stack is not empty.
  // Result: The most recent element is returned.
  // Effect: The most recent element is removed from the stack.
  def pop() : A
  // Precondition: Stack is not empty.
  // Result: The most recent element is returned.
  // Effect: None
  def top : A
  // Precondition: None
  // Effect: None
  // Result: true is returned if and only if the stack has no elements.
  def isEmpty : Boolean
  // Precondition: None
  // Effect: None
  // Result: The number of elements in the stack is returned.
  def size : Int
  //Precodition: Stack is not empty and of Type Klammern
  //Effect:None
  //Result: true is returned if the Stack is a valid Klammerausdruck


import scala.reflect.ClassTag
class DynamicArrayStack[A : ClassTag] extends MyStack[A]:
  // Header:
  private var array : Array[A] = new Array[A](1)
  private var amount : Int = 0
  // Precondition: None
  // Result: None
  // Effect: (array.length/8 <= amount < array.length) holds.
  private def resize() : Unit =
    val cap : Int = array.length
    if cap/8 <= amount && amount < cap then return // do nothing if INV holds
    // allocate a new array with quartered or quardrupled size of the old array:
    val newArray : Array[A] = new Array[A](if cap/8>amount then cap/4 else cap*4)
    // Copy all elements to new array:
    for i <- 0 to amount-1 do
      newArray(i) = array(i)
    array = newArray // the old array is now removed
  def push(x : A) : Unit =
      array(amount) = x
      amount = amount + 1
      resize() // Array too small? ... Resize!
  def pop() : A =
        if !isEmpty then
          val result : A = array(amount - 1)
          array(amount - 1) = null.asInstanceOf[A]
          amount = amount - 1
          resize() // Array too large? ... Resize!
          result
        else throw new Exception("Stack is empty")
  def isEmpty: Boolean = amount == 0
  def size: Int = amount
  def top: A = 
    if !isEmpty then array(amount - 1)
    else throw new Exception("Stack is empty")
  def cap: Int = array.length

@main
def testing():Boolean =
  val newLL = new DynamicArrayStack[Int]
  for (a <- 1 to 10){
    println("current cap: " + newLL.cap)
    newLL.push(1)
  }
  for (a <- 1 to 10){
    println("current cap: " + newLL.cap)
    newLL.pop()
  }
  return true
