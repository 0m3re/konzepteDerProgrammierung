/*
 * author: Julian Mueller, David Glaser
 * due Date: 26.01.2024
 */

// b)
class SimpleArrayQueue[T](initialCapacity: Int = 16):
  private var array: Array[Any] = new Array[Any](initialCapacity)
  private var front: Int = 0
  private var rear: Int = 0

  def enqueue(item: T): Unit = 
    if ((rear + 1) % array.length == front) 
      resize()
    
    array(rear) = item
    rear = (rear + 1) % array.length
  

  def dequeue(): Option[T] = 
    if (isEmpty) return None
    val item = array(front).asInstanceOf[T]
    front = (front + 1) % array.length
    Some(item)
  

  def isEmpty: Boolean = front == rear

  private def resize(): Unit = 
    val newArray: Array[Any] = new Array[Any](array.length * 2)
    for (i <- 0 until array.length) {
      newArray(i) = array((front + i) % array.length)
    }
    array = newArray
    front = 0
    rear = array.length / 2
  



// d)

class BooleanAttributeArrayQueue[T](initialCapacity: Int = 16):
  private var array: Array[Any] = new Array[Any](initialCapacity)
  private var front: Int = 0
  private var rear: Int = 0
  private var isFull: Boolean = false

  def enqueue(item: T): Unit = 
    if (isFull) 
      resize()
    
    array(rear) = item
    rear = (rear + 1) % array.length
    if (rear == front) 
      isFull = true
    
  

  def dequeue(): Option[T] = 
    if (isEmpty) return None
    val item = array(front).asInstanceOf[T]
    front = (front + 1) % array.length
    isFull = false
    Some(item)
  

  def isEmpty: Boolean = front == rear && !isFull

  private def resize(): Unit = 
    val newArray: Array[Any] = new Array[Any](array.length * 2)
    for (i <- 0 until array.length) 
      newArray(i) = array((front + i) % array.length)
    
    array = newArray
    front = 0
    rear = array.length / 2
    isFull = false

// e) 
class VIPQueue[T]:
  private var vipQueue: List[T] = List()
  private var normalQueue: List[T] = List()

  def enqueue(item: T, isVIP: Boolean = false): Unit =
    if (isVIP)
      vipQueue = vipQueue :+ item
    else
      normalQueue = normalQueue :+ item

  def dequeue(): Option[T] =
    if (vipQueue.nonEmpty)
      val vipItem = vipQueue.head
      vipQueue = vipQueue.tail
      Some(vipItem)
    else if (normalQueue.nonEmpty) 
      val normalItem = normalQueue.head
      normalQueue = normalQueue.tail
      Some(normalItem)
    else
      None

  def peek(): Option[T] = 
    if (vipQueue.nonEmpty)
      Some(vipQueue.head)
    else if (normalQueue.nonEmpty)
      Some(normalQueue.head)
    else
      None

  def isEmpty: Boolean = vipQueue.isEmpty && normalQueue.isEmpty
