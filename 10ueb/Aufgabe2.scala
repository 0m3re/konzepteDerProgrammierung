def mergeSort[T](list: List[T])(implicit ord: Ordering[T]): List[T] = 
    def merge(left: List[T], right: List[T]): List[T] = 
        (left, right) match 
            case (Nil, _) => right
            case (_, Nil) => left
            case (x :: xs, y :: ys) =>
                if (ord.lt(x, y)) x :: merge(xs, right)
                else y :: merge(left, ys)
  

    val n = list.length / 2
    if (n == 0) list
    else 
        val (left, right) = list.splitAt(n)
        merge(mergeSort(left), mergeSort(right))

object VielleichtNeMap extends App {
    enum Vielleicht[+T]:
      case Nichts
      case Wert(t : T)
    //map(Vielleicht[A], f:A=>B):Vielleicht[B]
    //Precondition: None
    //Effect: None
    //result: Recives an Element of Type Vielleicht and applies a given function to it and returns f(Vielleicht[A])
    //Test cases:
    //map(Vielleicht(Nichts), f(x)=>2*x) = Vielleicht(Nichts)
    //map(Vielleicht(1), f(x)=>2*x) = Vielleicht(2)
    def map[A,B](v:Vielleicht[A], f:A=>B): Vielleicht[B] = 
      v match
        case Nichts => return Nichts
        case Wert(t) => return Wert(f(t))
  
    //extract(List[Vielleicht[A]]):List[A]
    //Precondition: A List of Type Vielleicht[A]
    //Effect: None
    //result: extracts each Value of Type Vielleicht that is not Nichts and adds it to a List
    //Test cases:
    //map(Vielleicht(Nichts), f(x)=>2*x) = Vielleicht(Nichts)
    //map(Vielleicht(1), f(x)=>2*x) = Vielleicht(2)
    def extract[A](li:List[Vielleicht[A]]): List[A] =
      val newList:List[A] = List()
      li.foreach {
        case Nichts =>
        case Wert(t) => newList :+ t
      }
      return newList
}

object Goldchains extends App {
  enum Link:
    case G, S, P
  enum Chain:
    case Empty
    case Join(left : Chain, l : Link, right : Chain)

  def toList(cha:Chain):List[Link] = 
    def iterate(cha:Chain, li:List[Link]): List[Link] =  
      cha match
        case Chain.Empty => return li
        case Chain.Join(left, l, right) => {
          if(right != Chain.Empty) {
            iterate(right, li :+ l)
          } else {
            return li :+ l
          }
        }
    return iterate(cha, List())
  def p(l:Link):Int =
        l match
          case Link.G => return 1
          case Link.P => return 2
          case Link.S => return 3
        
  def priceIterate(cha:Chain):Number = 
    def help(chain:Chain, sum:Int):Int =
        chain match
          case Chain.Empty => return sum
          case Chain.Join(left, l, right) => {
            if(right != Chain.Empty) {
              help(right, sum+p(l))
            } else {
              return sum+p(l)
            }
          }
    return help(cha, 0)
  
  def priceWithList(cha:Chain):Integer =
    val newList = toList(cha).map(p)
    return newList.fold(0)((x,y) => x+y)
}
