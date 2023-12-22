//-----------------1a Teil 1

  //replace(Any, Any,List[Any]):List[Any]
  //Precondition: A non empty list
  //Effect: None
  //result: Returns a given list where each given element x is replaced with given element y
  //Test cases:
  //replace(1,2,List(1,2,3,4,5,6)) = List(2,2,3,4,5,6)
  //replace(1,2,List(3,4,5,6,7)) = List(3,4,5,6,7)
  //replace(1,2,list(1)) = List(2)
  def replace(a: Any, b:Any, list: List[Any]):List[Any] =
    def compareAndReplace(elem:Any):Any = {
      if (elem == a) {
        return b
      } else {
        return elem
      }
    }
    var neList: List[Any] = list.map(compareAndReplace)
    return neList



//------------------ 1a Teil 2

  //replaceR(Any, Any,List[Any]):List[Any]
  //Precondition: A non empty list
  //Effect: None
  //result: Returns a given list where each given element x is replaced with given element y
  //Test cases:
  //replaceR(1,2,List(1,2,3,4,5,6)) = List(2,2,3,4,5,6)
  //replaceR(1,2,List(3,4,5,6,7)) = List(3,4,5,6,7)
  //replaceR(1,2,list(1)) = List(2)
  println("entering replace")
  def replaceR(a:Any, b:Any, list:List[Any]):List[Any] = 
    def help(newList:List[Any], list:List[Any]):List[Any] = 
      list match
        case Nil => return newList
        case x::Nil => return newList:::List(x)
        case x::y => {
          if (x == a) 
            help(newList:::List(b),y)
          else
            help(newList:::List(x),y)
        }
    val helpList = List()
    help(helpList,list)



//------------------ 1b

  //isSorted((Any,Any)=>Boolean,List[Any]):Boolean
  //Precondition: A non empty list
  //Effect: None
  //result: Returns a Boolean if the list is sorted by the given precodition defined in comp
  //Test cases:
  //isSorted((_:Int)>(_:Int), List(4,3,2,1)) =true
  //isSorted((_:Int)>(_:Int), List(2,3,2,1)) =false
  def isSorted(comp:(Int,Int)=>Boolean, list:List[Int]):Boolean =
    def help(list:List[Int]):Boolean =
      list match 
        case Nil => return false
        case x::Nil => return true
        case x::y::z => if(comp(x,y)) { help(y::z) } else { return false }
    return help(list)



//------------------ 1c
  
  //findMyNumbers(takeNumbers(Int, List[Int])=>Int, List[Int]):List[Int]
  //Precondition: A non empty list, 
  //Effect: None
  //result: Returns the first n elements of the list. The hof takeNumbers defines the conditions of the selected elements.
  //Test cases:
  //findMyNumbers(takeNumbers, List(1,2,3,4,5,6)) => if you enter 3 => it returns List(1,2,3)
  import scala.io.StdIn.readLine
  def findMyNumbers(takeNumbers:(x:Int,l:List[Int])=>Int, list:List[Int]) =
    println("please insert a number: ")
    val y = readLine().toInt
    val sIndex = takeNumbers(y, list)
    println(list.take(sIndex))
  //takeNumbers(Int, List[Int]):Int
  //Precondition: A Non empty List and a given x which is < then the cross sum of the elements in the list, else the list is 0
  //Effect: None
  //result: This Function defines the index of the returned numbers in findMyNumbers. Here it returns the index where findMyNumbers will return the index 0-x
  //Test cases:
  //see find my numbers
  def takeNumbers(x:Int, list:List[Int]):Int =
    def help(acc:Int, index:Int, list:List[Int]):Int =
      if(x < acc) return index
      list match
            case Nil => return 0
            case y::Nil => if(acc+y < x ) { return 0 } else { return index+1}
            case y::ys => help(acc+y, index+1, ys)
    return help(0, 0, list)  



//------------------ 1d

  //foldTheListInReverse(List[Any]):List[Any]
  //Precondition: A non empty list
  //Effect: None
  //result: Returns the reversed List
  //Test cases:
  //foldTheListInReverse(List(1,2,3,4,5,6)) = List(6,5,4,3,2,1)
  //foldTheListInReverse(List(2,3,4)) = List(4,3,2)
  def foldTheListInReverse(list:List[Any]):List[Any] = 
    return list.foldLeft(List())((list:List[Any],x:Any) => x::list)
