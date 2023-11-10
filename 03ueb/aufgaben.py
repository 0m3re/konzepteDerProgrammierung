"""

"""
# Man haette alles wie gefragt in zwei Dateien schreiben können, aber wir haben Funktionen die wir für die Uebung 1 geschrieben haben in der Uebung 2 benutzt.
# Da wir noch keine Klassen gesehen habe, dachten wir uns es ist besser alles in eine Datei zu schreiben

import random
random.seed(0)

# Aufgabe 1
## a) Binaersuche
# bsearch(List[Number], Number): Number
# Precondition: Non empty List of int/float
# Effect: None
# Result: Returns the smallest element
'''Test cases
print(bsearch([1,2,3,5,78,132,56768],132)) == True
'''

#bsearch sortiert die Liste aufsteigend, prüft das jeweils erste und letzte Element gegen das gesuchte Element.
def bsearch(s_list, num):
    s_list.sort()
    if s_list[0]>num:
        return False
    elif s_list[len(s_list)-1]<num:
        return False
    else:
        return bsearch_calc(s_list, num)

# bsearch_calc(List[Number], Number): Number
# Precondition: Non empty List of int/float. The list must be sorted in ascending order
# Effect: None
# Result: Returns the smallest element
def bsearch_calc(s_list, num):
    print(s_list)
    length = len(s_list)
    mid = int(length/2)
    if s_list[mid] == num:
        return True
    elif length < 2:
        return False
    elif s_list[mid] > num:
        print("Rekursion - num < s_list[mid]")
        return bsearch_calc(s_list[:mid], num)
    elif s_list[mid] < num:
        print("Rekursion - num > s_list[mid]")
        return bsearch_calc(s_list[mid+1:], num)
      
# foo(List[Number], Number): Bool
# Precondition: Non empty List
# Effect: List elements will be rewritten with bool value
# Result: Returns False if there is a smaller number in the list, else False
def foo(xs, k):
    n = len(xs)
    for i in range(n):
        xs[i] = (xs[i] <= k)
    erg = False
    for b in xs:
        erg = b or erg
    return erg

# bar(List[Number], Number): Bool
# Precondition: Non-empty list
# Effect: None
# Result: Returns True if any number in the list is less than or equal to `k`, else False.
def bar(xs, k):
    n = len(xs)
    erg = False
    for i in range(n):
        erg = (xs[i] <= k) or erg
    return erg

# recursive_bar(List[Number], Number):Bool
# Precondition: Non empty List
# Effect: None
# Result: Returns False if there is a smaller number in the list, else False
def recursive_bar(xs, x):
    if len(xs)>2:
        return xs[0]>x
    else:
      return xs[0]>x and recursive_bar(x[:1], x)

## c) Funktion add
# add(List[int], List[int]): (List[int], int)
# Precondition: None
# Effect: Prints a message if the lengths of the two lists are different.
# Result: Returns a tuple containing two elements. 
#         The first element is a list with the Component-wise sum of the elements of list1 and list2.
#         The second element is the scalar product of list1 and list2.
""" Test cases:
add([1, 2, 3], [4, 5, 6]) == ([5, 7, 9], 32)
add([1, 2, 3], [1, 2]) == ([2, 4], 5)
add([1, 2], [1, 2, 3]) == ([2, 4], 5)
"""
def add(list1, list2):
    sum_list = []
    scalar_product = 0
    if len(list1) != len(list2):
        print("Sie haben zwei verschiedene Größen angegeben. Die Zahlen, die es zu viel gibt, werden dann einfach weggelassen.")
        length = min(len(list1), len(list2)) 
    else: 
        length = len(list1)
    for i in range(length):
        sum_list.append(list1[i] + list2[i])
        scalar_product += list1[i] * list2[i]
    return sum_list, scalar_product

## d) Funktion countDigits
# countDigits_with_effect(int): int
# Precondition: number is non-negative.
# Effect: Converts the number to a string.
# Result: Returns the number of digits in the given number.
""" Test cases:
countDigits_with_effect(12345) == 5
countDigits_with_effect(1000) == 4
countDigits_with_effect(0) == 1
"""
def countDigits_with_effect(number):
    return len(str(number))

# countDigits(int): int
# Precondition: number is non-negative.
# Effect: None
# Result: Returns the number of digits in the given number.
""" Test cases:
countDigits(12345) == 5
countDigits(1000) == 4
countDigits(0) == 0
"""
def countDigits(number):
    counter = 0
    while number > 0:
        number = number // 10
        counter += 1
    return counter

# Aufgabe 2
## a) Binaersuche
### Siehe Aufgabe 1 a) 
### Anstatt den Algorithmus neu zu schreiben, ist es einfacher die Liste zu sortieren damit es passt. Ansonsten haette man den selben Algorithmus schreiben muessen der das gegenteil macht.

## b) ggt

# ggt(int, int): int
# Precondition: number1 and number2 can't be negative and one of them not zero.
# Effect: Prints each step of the algorithm to the terminal.
# Result: Returns the greatest common divisor of number1 and number2
""" Test cases:
ggt(48, 18) == 6
ggt(0, 5) == 5
ggt(7, 7) == 7
"""
def ggt(number1, number2):
    if number1 > number2:
        x, y = number2, number1
    else: 
        x, y = number1, number2
    counter = 1
    while x != 0:
        r = y % x
        q = (y - r) // x # Ist nicht essentiell, macht aber die Ausgabe verständlicher
        print(f"\nSchritt {counter}: {y} = {q} * {x} + {r}")
        y, x = x, r
        counter += 1 # hier das selbe
    return y

## c) dna2rna

# dna2rna_with_return(List[str]) : List[str]
# Precondition: list is not empty and list contains only iterations of 'A', 'C', 'G', 'T'.
# Effect: None 
# Result: Returns a list, where each 'T' has been replaced with 'U'.
""" Test cases:
dna2rna_with_return(["A", "T", "G", "T", "C", "A"]) == ["A", "U", "G", "U", "C", "A"]
dna2rna_with_return(["A", "C", "G", "C", "A"]) == ["A", "C", "G", "C", "A"]
dna2rna_with_return(["T", "T", "T", "T"]) == ["U", "U", "U", "U"]
"""
def dna2rna_with_return(dna_sequenz):
    rna_sequenz = []
    for i in dna_sequenz:
        if i == "T":
            rna_sequenz.append("U")
        else:
            rna_sequenz.append(i)
    return rna_sequenz

# dna2rna_without_return(List[str]) : None
# Precondition: list is not empty and list contains only iterations of 'A', 'C', 'G', 'T'.
# Effect: Modifies the input list directly, replacing each 'T' with 'U'.
# Result: Each 'T' in the input list is replaced with 'U'.
""" Test cases:
dna_sequence = ["A", "T", "G", "C", "T", "A"]
dna2rna_without_return(dna_sequence)
dna_sequence == ["A", "U", "G", "C", "U", "A"] 

dna_sequence = ["A", "C", "G", "C", "A"]
dna2rna_without_return(dna_sequence)
dna_sequence == ["A", "C", "G", "C", "A"]

dna_sequence = ["T", "T", "T", "T"]
dna2rna_without_return(dna_sequence)
dna_sequence == ["U", "U", "U", "U"] 
"""
def dna2rna_without_return(dna_sequenz):
    for i in range(len(dna_sequenz)):
        if dna_sequenz[i] == "T":
            dna_sequenz[i] = "U"

## d) smallest - void
# smallest(List[Number]):Number
# Precondition: Non empty list; Number of type int or float
# Effect: The num_list Object will be changed and everything but the smallest element will be deleted.
# Result: None
''' Test cases:
smallest([1,2,3,6,98,0]) => num_list == [0]
smallest([9,827,1,3,5,7,1,-1]) => num_list == [-1]
smallest([1]) => num_list == [1]
smallest([1.0,1.3.0.3.10.5]) => num_list == [0.3]
'''

def smallest(num_list):
    # Abbruchsbedingung für Liste < 2.
    if len(num_list)<2:
          None
    # Vergleich der jeweils ersten beiden Elemente der List - das größere wird entfernt.
    elif num_list[0] < num_list[1]:
        del num_list[1]
        smallest(num_list)
    else:
        del num_list[0]
        smallest(num_list)
          
## d 2) smallest - No Effect
# smallest(List[Number]):Number
# Precondition: Non empty list; Number of type int or float
# Effect: None
# Result: The smallest number in a List of numbers is returned
''' Test cases:
k_smallest([1,2,3,6,98,0]) == 0
k_smallest([9,827,1,3,5,7,1,-1) == -1
k_smallest([1]) == 1
l_smallest([1.0,1.3.0.3.10.5]) == 0.3
'''
def k_smallest(num_list):
    # Abbruchsbedingung für Liste < 2.
    if len(num_list)<2:
        return num_list[0]
    # Vergleich der jeweils ersten beiden Elemente der List - das größere wird entfernt.
    elif num_list[0] < num_list[1]:
        return k_smallest(num_list[:1]+num_list[2:])
    else:
        return k_smallest(num_list[1:])

## e) quersumme

# quersumme(int) : int
# Precondition: None
# Effect: None
# Result: The function returns the sum of the digits of number.
""" Test cases:
quersumme(123) == 6
quersumme(0) == 0
quersumme(505) == 10
quersumme(-123) == -6
"""
def quersumme(number):
    if number > 10:
        return (number%10) + quersumme(number//10)
    elif number < -10:
        return (number%-10) - quersumme((number//-10))
    else: 
        return number

## Utils Funktionen
# generate_random_number_list(int, int, int): List[int]
# Precondition: 'size' is a non-negative integer, 'smallest' and 'biggest' are integers and biggest is greter than smallest
# Effect: None.
# Result: Returns a list of random integers of length 'size'. Each integer is in the range between 'smallest' and 'biggest'.
def generate_random_number_list(size, smallest, biggest):
    number_list = []
    for _ in range(size):
        number_list.append(random.randint(smallest, biggest))
    return number_list


# Main Teil des Programms

def main():
    while True:
        print("Auswahl:\n"
              "1: Aufgabe 1\n"
              "2: Aufgabe 2\n"
              "3: Exit")
        user_choice = input("Was möchtest du Wählen: ")
        if user_choice == "1":
            aufgabe1()
        elif user_choice == "2":
            aufgabe2()
        elif user_choice == "3":
            exit()
        else:
            print("Bitte gebe eine Zahl zwischen 1 und 3 ein.")

def aufgabe1():
    while True:
        print("Auswahl:\n"
              "1: Binaersuche\n"
              "2: foo/bar\n"
              "3: add\n"
              "4: countDigits\n"
              "5: Zurueck")
        user_choice = input("Was möchtest du Wählen: ")
        if user_choice == "1":
            search_list = [1, 2, 4, 8, 16, 32, 42, 64, 128, 130, 243, 244, 289]
            number = 2
            print("Wir suchen in der vorgegebenen Liste:", search_list)
            found = bsearch(search_list, number)
            print("Wurde die gesuchte Zahl", number, "in der Liste gefunden:", found)
        elif user_choice == "2":
            xs = []
            size = int(input("Wie groß soll die Liste sein: "))
            smallest = int(input("Was ist die untere Schranke der Liste: "))
            biggest = int(input("Was ist die obere Schranke der Liste: "))
            xs = generate_random_number_list(size, smallest, biggest)
            k = int(input("Gebe die Zahl für k ein: "))
            print("Die generierte Liste", xs)
            print("Funktion foo: ", foo(xs, k))
            print("Imperative bar Funktion: ", bar(xs, k))
            print("Recursive bar Funktion", recursive_bar(xs, k))
        elif user_choice == "3":
            size_first_list = int(input("Gebe ein, wie groß die erste Liste sein soll: "))
            smallest_first = int(input("Was ist die untere Schranke der Liste: "))
            biggest_first = int(input("Was ist die obere Schranke der Liste: "))
            size_second_list = int(input("Gebe ein, wie groß die zweite Liste sein soll: "))
            smallest_second = int(input("Was ist die untere Schranke der Liste: "))
            biggest_second = int(input("Was ist die obere Schranke der Liste: "))
            first_number_list = generate_random_number_list(size_first_list, smallest_first, biggest_first)
            second_number_list = generate_random_number_list(size_second_list, smallest_second, biggest_second)
            print("Die erste generierte Liste", first_number_list)
            print("Die zweite generierte Liste", second_number_list)
            sum_list, skalar_produkt = add(first_number_list, second_number_list)
            print("Die komponenten weise Summe der Liste ist", sum_list, "und das Skalarprodukt ist", skalar_produkt)
        elif user_choice == "4":
            number = input("Geben Sie eine Zahl ein: ")
            result = countDigits(number)
            print("Die Anzahl an Dezimalstellen ist", result)
        elif user_choice == "5":
            break
        else:
            print("Bitte gebe eine Zahl zwischen 1 und 3 ein.")

def aufgabe2():
    while True:
        print("Auswahl:\n"
              "1: Binaersuche\n"
              "2: ggt\n"
              "3: dna2rna\n"
              "4: k_smallest\n"
              "5: quersumme\n"
              "6: Zurueck")
        user_choice = input("Was möchtest du Wählen: ")
        if user_choice == "1":
            search_list = [289, 244, 243, 130, 128, 64, 42, 32, 16, 8, 4, 2, 1]
            number = 2
            print("Wir suchen in der vorgegebenen Liste:", search_list)
            found = bsearch(search_list, number)
            print("Wurde die Zahl", number, "in der Liste gefunden", found)
        elif user_choice == "2":
            print("Die Formel des euklidischen Algorithmus ist wie folgt: r(n-1) = quotient(n+1) * r(n) + r(n+1)")
            print("Berechnung des GGT für 1215 und 2745:")
            result = ggt(1215, 2745)
            print("\nDer größte gemeinsame Teiler (GGT) ist", result)
        elif user_choice == "3":
            dna_sequenz = list(input("Gebe die DNA-Sequenz ein, die du umwandeln möchtest: ").upper())
            rna_sequenz = dna2rna_with_return(dna_sequenz)
            print("Konvertierte Sequenz (unveränderte Originalsequenz):", rna_sequenz)
            print("Original DNA-Sequenz:", dna_sequenz)
            dna2rna_without_return(dna_sequenz)
            print("Konvertierte DNA-Sequenz (veränderte Originalsequenz):", dna_sequenz)
        elif user_choice == "4":
            size = int(input("Wie groß soll die Liste sein: "))
            smallest = int(input("Was ist die untere Schranke der Liste: "))
            biggest = int(input("Was ist die obere Schranke der Liste: "))
            random_number_list = generate_random_number_list(size, smallest, biggest)
            print("Die generierte Liste:", random_number_list)
            result = k_smallest(random_number_list) 
            print("Das kleinste Element der Liste ist", result)
        elif user_choice == "5":
            number = int(input("Gebe eine Zahl ein, um die Quersumme zu berechnen: "))
            result = quersumme(number)
            print(f"Die Quersumme von {number} ist {result}.")
        elif user_choice == "6":
            break
        else:
            print("Bitte gebe eine Zahl zwischen 1 und 3 ein.")

main()
