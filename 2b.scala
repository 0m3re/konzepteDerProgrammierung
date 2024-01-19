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
