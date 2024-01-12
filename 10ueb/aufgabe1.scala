/* 
 * Uebungsblatt 10
 * author: Julian und David Glaser
 * due date: 2024-01-12
 */

// Aufgabe a)
def verifySort[T](list: List[T])(implicit ord: Ordering[T]): Boolean = 
    list match 
        case Nil | _ :: Nil => true
        case head :: tail => tail match 
            case next :: _ if ord.lteq(head, next) => verifySort(tail)
            case _ => false

// Aufgabe b)
def sumSmaller[T](list: List[T], w: T)(implicit num: Numeric[T]): T = 
    list match 
        case Nil => num.zero
        case head :: tail if num.lt(head, w) => num.plus(head, sumSmaller(tail, w))
        case _ :: tail => sumSmaller(tail, w)

// Aufgabe c)
enum EntwederOder[+A, +B]:
    case Links(value: A)
    case Rechts(value: B)


// EntwederOder kann für Fehlerbehandlung verwendet werden, um Fehlermeldungen zu übergeben.

def parseInteger(str: String): EntwederOder[String, Int] = 
    try 
        EntwederOder.Rechts(str.toInt)
    catch
        case _: NumberFormatException => EntwederOder.Links(s"Konnte '$str' nicht in Integer umwandeln")

def dateiExistiert(filePath: String): EntwederOder[String, Boolean] = 
    val file = new java.io.File(filePath)

    if (file.exists()) EntwederOder.Rechts(true)
    else EntwederOder.Links(s"Datei '$filePath' existiert nicht")

// Aufgabe d)

enum BoolExpr:
    case True
    case False
    case Or(left: BoolExpr, right: BoolExpr)
    case And(left: BoolExpr, right: BoolExpr)
    case Not(expr: BoolExpr)

    def eval: BoolExpr = 
        this match 
            case True => True
            case False => False
            case Or(left, right) =>
                (left.eval, right.eval) match 
                    case (False, False) => False // Eizige case, wo "or" false zurückgeben kann
                    case _ => True
            
            case And(left, right) =>
                (left.eval, right.eval) match 
                    case (True, True) => True // Eizige case, wo "and" true zurückgeben kann
                    case _ => False
            
            case Not(expr) => 
                expr.eval match 
                    case True => False
                    case False => True

    def negateVals: BoolExpr = 
        this match 
            case True => False
            case False => True
            case Or(left, right) => Or(left.negateVals, right.negateVals)
            case And(left, right) => And(left.negateVals, right.negateVals)
            case Not(expr) => Not(expr.negateVals)

// Aufgabe e)

def splitAt[A](list : List[A], i : Int) : (List[A], List[A]) =
    (list, i) match
        case (Nil, _) =>
            (Nil, Nil) // (*)
        case (_, 0) =>
            (Nil, list) // (*)
        case (x::xs, i) =>
            val (left, right) = splitAt(xs, i-1)
            (x::left, right) // (*)

// Signatur: def splitAt[A](list: List[A], i: Int): (List[A], List[A])
// Precondition: i >= 0



// @main def tests = {
//     println(verifySort(List(1, 2, 7, 4, 5, 6)))
//     println(sumSmaller(List(1, 2, 7, 4, 5, 6), 5))
//     val ergebnis1 = parseInteger("123")
//     val ergebnis2 = parseInteger("abc")
//     val ergebnis3 = dateiExistiert("nichtExistierendeDatei.txt")
//     val ergebnis4 = dateiExistiert("aufgabe1.scala") 
//     println(ergebnis1)
//     println(ergebnis2)
//     println(ergebnis3)
//     println(ergebnis4)
//     val expr = BoolExpr.And(BoolExpr.True, BoolExpr.Not(BoolExpr.True))
//     val expr2 = BoolExpr.Or(BoolExpr.True, BoolExpr.And(BoolExpr.True, BoolExpr.False))
//     println(expr.eval)
//     println(expr.negateVals)
//     println(expr2.eval)
//     println(expr2.negateVals)
// }