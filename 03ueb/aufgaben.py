"""

"""
# Man haette alles wie gefragt in zwei Dateien schreiben können, aber wir haben Funktionen die wir für die Uebung 1 geschrieben haben in der Uebung 2 benutzt.
# Da wir noch keine Klassen gesehen habe, dachten wir uns es ist besser alles in eine Datei zu schreiben

import random
random.seed(0)

# Aufgabe 1
## a) Binaersuche
def bsearch(s_list, num):
    s_list.sort()
    if s_list[0]>num:
        return False
    elif s_list[len(s_list)-1]<num:
        return False
    else:
        return bsearch_calc(s_list, num)

def binaer_suche(number_list, number):
    number_list.sort()
    right = len(number_list) - 1
    left = 0
    while left <= right:
        center = (right + left)//2
        if number_list[center] == number:
            return True
        elif number_list[center] > number:
            right = center - 1
        else:
            left = center + 1
    else:
        return False
 
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
      
def foo(xs, k):
    """
    Ueberprueft ob eine gegebene Zahl kleiner ist als alle in der Liste enthaltenen Zahlen ist, 
    wenn ja gebe False aus ansonsten True.
    """
    n = len(xs)
    for i in range(n):
        xs[i] = (xs[i] <= k)
    erg = False
    for b in xs:
        erg = b or erg
    return erg

def bar(xs, k):
    n = len(xs)
    erg = False
    for i in range(n):
        erg = (xs[i] <= k) or erg
    return erg

def recursiv_bar(xs, k, erg = False):
    if len(xs) > 0:
        return recursiv_bar(xs[1:], k, (xs[0] <= k) or erg)
    else:
        return erg

## c) Funktion add
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
    return "Komponentenweise Summe:", sum_list, "Skalar Produkt:", scalar_product

## d) Funktion countDigits
def countDigits_with_conversion(number):
    return len(str(number))

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
def ggt(number1, number2):
    if number1 > number2:
        number1, number2 = number2, number1
    counter = 1
    while number1 != 0:
        r = number2 % number1
        q = (number2 - r) // number1 # Ist nicht essentiell, macht aber die Ausgabe verständlicher
        print(f"\nSchritt {counter}: {number2} = {q} * {number1} + {r}")
        number2, number1 = number1, r
        counter += 1 # hier das selbe
    return number2

## c) dna2rna

# dna2rna_with_return(List[str]): List[str]
# Precondition: list is not empty, list does only contain iterations of A, C, T, G
# Effect: None
# Result: The rna sequenz is returned (the same as input, but T replaced by U)
''' Test cases:
dna2rna_with_return(["A", "T", "G", "T", "C", "A"]) == ["A", "U", "G", "U", "C", "A"]
dna2rna_with_return(["A", "C", "T", "T", "A", "C"]) == ["A", "C", "U", "U", "A", "C"]
dna1rna_with_return(["G", "T", "T", "A", "C", "G", "A", "T", "C"]) == ["G", "U", "U", "A", "C", "G", "A", "U", "C"]
'''
def dna2rna_with_return(dna_sequenz):
    rna_sequenz = []
    for i in dna_sequenz:
        if i == "T":
            rna_sequenz.append("U")
        else:
            rna_sequenz.append(i)
    return rna_sequenz

def dna2rna_without_return(dna_sequenz):
    for i in range(len(dna_sequenz)):
        if dna_sequenz[i] == "T":
            dna_sequenz[i] = "U"

## d) k_smallest
def k_smallest(number_list, tmp = None):
    if tmp == None:
        tmp = number_list[0]
        return k_smallest(number_list[1:], tmp)
    if len(number_list) > 0:
        if number_list[0] < tmp:
            tmp = number_list[0]
        return k_smallest(number_list[1:], tmp)
    else:
        return tmp

## e) quersumme
def quersumme(number):
    x = number
    if x > 0:
        return (x%10) + quersumme(x//10)
    else: 
        return x 

## Utils Funktionen
def create_number_list(text, length):
    number_list = []
    for _ in range(length):
        number = input(text)
        number_list.append(number)
    return number_list

def generate_random_number_list(size, smallest, biggest):
    if smallest > biggest:
        smallest, biggest = biggest, smallest
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
            position = binaer_suche(search_list, number)
            print(f"Die Nummer {number} wurde an der Position {position} gefunden.")
        elif user_choice == "2":
            xs = []
            length = input("Wie viele Zahle sollen in der Liste enthalten sein: ")
            xs = create_number_list("Gebe die nächste Zahl ein: ", length)
            k = input("Gebe die Zahl für k ein: ")

            print("Funktion foo: ", foo(xs, k))
            print("Imperative bar Funktion: ", bar(xs, k))
            print("Recursive bar Funktion", recursiv_bar(xs, k))
        elif user_choice == "3":
            size_first_list = int(input("Gebe ein, wie viele Zahlen in der ersten Liste sein sollen: "))
            size_second_list = input("Gebe ein, wie viele Zahlen in der zweiten Liste sein sollen: ")

            print("Zahlen für die erste Liste:")
            first_number_list = create_number_list("Gebe die nächste Zahl ein: ", size_first_list)

            print("Zahlen für die zweite Liste:")
            second_number_list = create_number_list("Gebe die nächste Zahl ein: ", size_second_list)

            print(add(first_number_list, second_number_list))
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
            position = binaer_suche(search_list.sort(), number)
            print(f"Die Nummer {number} wurde an der Position {position} gefunden.")
        elif user_choice == "2":
            print("Die Formel des euklidischen Algorithmus ist wie folgt: r(n-1) = quotient(n+1) * r(n) + r(n+1)")
            print("Berechnung des GGT für 1215 und 2745:")
            result = ggt(1215, 2745)
            print("\nDer größte gemeinsame Teiler (GGT) ist", result)
        elif user_choice == "3":
            dna_sequenz = list(input("Gebe die DNA-Sequenz ein, die du umwandeln möchtest: ").upper())
            if input(dna_sequenz):
                rna_sequenz = dna2rna_with_return(dna_sequenz)
                print("Konvertierte Sequenz (unveränderte Originalsequenz):", rna_sequenz)
                print("Original DNA-Sequenz:", dna_sequenz)
                dna2rna_without_return(dna_sequenz)
                print("Konvertierte DNA-Sequenz (veränderte Originalsequenz):", dna_sequenz)
            else:
                print("Die eingegebene Sequenz enthält ungültige Zeichen. Bitte geben Sie nur A, T, G oder C ein.")
        elif user_choice == "4":
            size = input("Wie groß soll die Liste sein.")
            smallest = input("Was ist die untere Schranke der Liste.")
            biggest = input("Was ist die obere Schranke der Liste.")
            random_number_list = generate_random_number_list(size, smallest, biggest)
            result = k_smallest(random_number_list) 
            print("Das kleinste Element der Liste ist", result)
            number = input("Gebe eine Zahl ein, um die Quersumme zu berechnen: ")
        elif user_choice == "5":
            result = quersumme(number)
            print(f"Die Quersumme von {number} ist {result}.")
        elif user_choice == "6":
            break
        else:
            print("Bitte gebe eine Zahl zwischen 1 und 3 ein.")

main()
