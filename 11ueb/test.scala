class Place:
    def printMe() = println("Buy it.")
class Region extends Place:
    override def printMe() = println("Box it.")
class State extends Region:
    override def printMe() = println("Ship it.")
class Maryland extends State:
    override def printMe() = println("Read it.")
@main
def test: Unit =
    var mid: Region = State()
    var md: State = Maryland()
    var obj: Any = Place()
    var usa: Place = Region()
    md.printMe()
    mid.printMe()
    obj.asInstanceOf[Place].printMe()
    obj = md
    obj.asInstanceOf[Maryland].printMe()
    obj = usa
    obj.asInstanceOf[Place].printMe()