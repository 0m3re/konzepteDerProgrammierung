

/* 
a) Spezifiziere den ADT PairPrioQueue, wenn in diesem Schlüssel-Wert-Paare gespeichert werden (vgl. erstes Video der Einheit). 
Die beiden wichtigen Funktionen haben die folgenden Signaturen:
Hier muss K eine Instanz der Klasse Ordering sein. Der Datentyp V hat keinerlei Einschränkungen.
*/
trait MyPrioQueue[K : Ordering, V]:
  // In a PrioQueue we store elements from a totally // ordered universe.
  // Precondition: None
  // Effect: The key-value-pair {key:value} is added to the priority queue. 
  // Result: None
  def insert(key : K, value: V) : Unit
  // Precondition: The queue is non-empty.
  // Effect: The element with the smallest k is removed from the queue 
  // Result: The element with the smallest k is returend
  def extractMin() : V
  // Precondition: None
  // Effect: None
  // Result: true is returned if and only if // the priority queue has no elements.
  def isEmpty : Boolean


/* 
b) Implementiere den ADT PairPrioQueue mit Hilfe der zweiten Variante der LinkedNodes. Nutze dabei die Dummyknoten-Technik. 
Ein Knoten sieht dann wie folgt aus:

*/

trait MyPrioQueue[K : Ordering, V]:
  // In a PrioQueue we store elements from a totally // ordered universe.
  // Precondition: None
  // Effect: The key-value-pair {key:value} is added to the priority queue. 
  // Result: None
  def insert(key : K, value: V) : Unit
  // Precondition: The queue is non-empty.
  // Effect: The element with the smallest k is removed from the queue 
  // Result: The element with the smallest k is returend
  def extractMin() : V
  // Precondition: None
  // Effect: None
  // Result: true is returned if and only if // the priority queue has no elements.
  def isEmpty : Boolean


class LinkedRandomNodes[K: Ordering, V]() extends MyPrioQueue[K,V]:
  import math.Ordering.Implicits.infixOrderingOps
  private class Node(val key : K, val value : V, var next : Node)
  private var anchor: Node = Node(null.asInstanceOf[K],null.asInstanceOf[V],null)
  def isEmpty: Boolean = anchor.next == null
  def extractMin(): V = 
    var temp : Node = anchor
    var smallest:Node = anchor.next
    while temp.next != null do
      if (temp.key > temp.next.key)
        smallest = temp.next
      temp = temp.next
  
    temp = anchor
    while true do
      if (temp.next.key == smallest.key)
        temp.next = temp.next.next
      temp = temp.next
    return smallest.value
  def insert(key: K, value: V): Unit = 
    var newNode:Node = Node(key, value, anchor.next)
    anchor.next = newNode


import scala.compiletime.ops.string
/* 
c) Verwende den ADT PairPrioQueue um den ADT Stack zu implementieren.
 */

trait MyPrioQueue[K : Ordering, V]:
  // In a PrioQueue we store elements from a totally // ordered universe.
  // Precondition: None
  // Effect: The key-value-pair {key:value} is added to the priority queue. 
  // Result: None
  def insert(key : K, value: V) : Unit
  // Precondition: The queue is non-empty.
  // Effect: The element with the smallest k is removed from the queue 
  // Result: The element with the smallest k is returend
  def extractMin() : V
  // Precondition: None
  // Effect: None
  // Result: true is returned if and only if // the priority queue has no elements.
  def isEmpty : Boolean

trait MyPPQStack[K:Ordering, V] extends MyPrioQueue[K, V]:
  //Precondition:None
  //Effect: A new Node with value V will be pushed to the beginning of the Queue
  //Result: None
  def push(value: V): Unit
  //Precondition: Non Empty Queue
  //Effect: Removes the first element from the queue
  //Result: Returns the value of the first element
  def pop(): V
  //Precondition:None
  //Effect: None
  //Result: Returns the current size of the Queue
  def size:Int

class LinkedNodes[K:Ordering, V]() extends MyPPQStack[K,V]:
  import math.Ordering.Implicits.infixOrderingOps
  private class Node(val key : K, val value : V, var next : Node)
  private var anchor: Node = Node(null.asInstanceOf[K],null.asInstanceOf[V],null)
  var size: Int = 0
  def isEmpty: Boolean = anchor.next == null
  def extractMin(): V = 
    var temp : Node = anchor
    var smallest:Node = anchor.next
    while temp.next != null do
      if (temp.key > temp.next.key)
        smallest = temp.next
      temp = temp.next
  
    temp = anchor
    while true do
      if (temp.next.key == smallest.key)
        temp.next = temp.next.next
      temp = temp.next
    return smallest.value
  def insert(key: K, value: V): Unit = 
    var newNode:Node = Node(key, value, anchor.next)
    anchor.next = newNode
    size = size +1
  def push(value: V): Unit = 
    insert(null.asInstanceOf[K],value)
  def pop(): V = 
    if isEmpty then throw Exception("Queue is empty") 
    val result : V = anchor.next.value
    anchor.next = anchor.next.next
    result
  
@main
def test123(): Unit = 
  var newStack = new LinkedNodes[Int, String]
  newStack.push("geht ")
  newStack.push("was ")
  newStack.push("Moin ")
  print(newStack.pop())
  print(newStack.pop())
  print(newStack.pop())
