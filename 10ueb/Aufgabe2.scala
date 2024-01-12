


object VielleichtNeMap extends App {
  enum Vielleicht[+T]:
    case Nichts
    case Wert(t : T)

    def map[A,B](v:Vielleicht[A], f:A=>B): Vielleicht[B] = 
      v match
        case Nichts => return Nichts
        case Wert(t) => return Wert(f(t))
    
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
