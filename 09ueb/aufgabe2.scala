
// Ich habe dieses Mal keine Klammern benutzt, aber ich verstehe immer noch nicht, wieso es in Scala 3 abgeschafft wurde. 
// Ich finde den Code ohne die Klammern schlechter lesbar, aber wenn es eine Konvention ist, dann richte ich mich nach ihr.

def partition[A](p : A => Boolean, list : List[A]): (List[A], List[A]) =
    def helper(remaining : List[A], passed : List[A], failed : List[A]): (List[A], List[A]) =
        remaining match
            case Nil => (passed, failed)
            case head::tail if p(head) => helper(tail, head::passed, failed)
            case head::tail => helper(tail, passed, head::failed)
    helper(list, Nil, Nil)

/* Einfache Variante
def lconcat[A](lists : List[List[A]]): List[A] =
    lists.flatten
*/

def lconcat[A](lists : List[List[A]]): List[A] =
    def helper(remaining: List[List[A]], acc: List[A]): List[A] = 
        remaining match
            case Nil => acc
            case head::tail => helper(tail, acc:::head)
    helper(lists, Nil)

def argmax(g: Int => Int, xs: List[Int]): Int =
    def helper(remaining: List[Int], x: Int): Int =
        remaining match
            case Nil => x
            case head::tail if g(head) > g(x) => helper(tail, head)
            case head::tail => helper(tail, x)
    if (xs.isEmpty) throw new IllegalArgumentException("Die Liste darf nicht leer sein.") // Man hätte auch eine Standard Zahl ausgeben können.
    else helper(xs.tail, xs.head)

def foldr[A,B](f : (A,B)=>B, e : B, list : List[A]) : B =
    list match
        case Nil => e
        case x::xs => f(x, foldr(f,e,xs))
def foldl[A,B](f : (B,A)=>B, e : B, list : List[A]) : B =
    list match
        case Nil => e
        case x::xs => foldl(f, f(e,x), xs)

@main def main() = 
    val nums = List(1, 2, 3, 4, 5)
    val predicate: Int => Boolean = x => x % 2 == 0
    val (even, odd) = partition(predicate, nums)
    println("Praedikat konform: " + even)
    println("Nicht Praedikat konform: " + odd)

    val listoflists = List(List(1, 3), List(4, 5), Nil, List(3))
    println(lconcat(listoflists))

    val xs = List(1, 4, 7, 3, 11, 5, 16, 0, 13)
    val f: Int => Int = x => x * x + 2 * x - 5
    println(argmax(f, xs))

    println(foldr((x:Int,rek:List[Int])=>x::rek, Nil, List(1,2,3,4)))
    /* 
    1. foldr(f, Nil, List(1,2,3,4))
    2. f(1, foldr(f, Nil, List(2,3,4)))
    3. f(1, f(2, foldr(f, Nil, List(3,4))))
    4. f(1, f(2, f(3, foldr(f, Nil, List(4)))))
    5. f(1, f(2, f(3, f(4, foldr(f, Nil, List())))))
    6. f(1, f(2, f(3, f(4, Nil)))) (da foldr(f, Nil, List()) zu Nil ausgewertet wird)
    7. f(1, f(2, f(3, List(4))))
    8. f(1, f(2, List(3,4)))
    9. f(1, List(2,3,4))
    10. List(1,2,3,4)
     */
    println(foldl((rek:List[Int],x:Int)=>x::rek, Nil, List(1,2,3,4)))
    /* 
    1. foldl(f, Nil, List(1,2,3,4))
    2. foldl(f, f(Nil, 1), List(2,3,4))
    3. foldl(f, f(f(Nil, 1), 2), List(3,4))
    4. foldl(f, f(f(f(Nil, 1), 2), 3), List(4))
    5. foldl(f, f(f(f(f(Nil, 1), 2), 3), 4), List())
    6. f(f(f(f(Nil, 1), 2), 3), 4) 
    7. f(f(f(List(1), 2), 3), 4)
    8. f(f(List(2,1), 3), 4)
    9. f(List(3,2,1), 4)
    10. List(4,3,2,1)
     */