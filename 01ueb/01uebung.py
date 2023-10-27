"""
Uebungsblatt 1
Autors: Julian Mueller, Marc Lambertz und David Glaser
Datum: ---
Beschreibung: In dieser Python File sind die Antworten für die Aufgaben 1, 2 und 3 Teil a.
"""

# Aufgabe 1
## a.
print("Aufgabe 1a:")
print("Calculate the area of a triangle.")
userInput = input("Enter the length of the side of the triangle: ")
userInput2 = input("Enter the heigth of the triangle: ")
try:
    a = int(userInput)
    ha = int(userInput2)
except ValueError:
    print("Please enter a valid number!")
    exit()
    
flaecheDreieck = (a * ha)/2

print(f"The area of the triangle is {flaecheDreieck}.")

## b.
"""
Man can switch case ausdruecke in Python mit if-elif-else statements ersetzen.
In dem Beispiel wird es mit einem Basic calculator gezeigt.
"""
print("\nAufgabe 1b:")
print("Example of a Switch Case in Python with a Basic Calculator.")
try:
    x = int(input("Enter a number for x: "))
    y = int(input("Enter a number for y: "))
except ValueError:
    print("Please enter a valid number!")
    exit()
operator = input("Enter the Operator of your choice (+, -, *, /): ")

if operator== "+":
    print(f"the result is {x+y}")
elif operator == "-": 
    print(f"the result is {x-y}")
elif operator == "*": 
    print(f"the result is {x*y}")
elif operator == "/": 
    print(f"the result is {x/y}")
else:
    print(f"The user input {userInput} is not a valid option.")

## c.
print("\nAufgabe 1c:")
print("Example of a for i in range with a while loop.")
i= 1
n = 10
while(i < n):
    print(i)
    i += 1

## d.
print("\nAufgabe 1d:")
print("Gebe 3 Zahlen und es wird True ausgegeben, wenn alle Zahlen verschieden sind.")
number1 = input(f"Enter a number:")
number2 = input(f"Enter a number:")
number3 = input(f"Enter a number:")
try:
    number2 = int(number1)
    number2 = int(number2)
    number3 = int(number3)
except ValueError:
    print("Please enter a valid number!")
    exit()
if number1 != number2 and number1 != number3 and number2 != number3:
    print(True)
else:
    print(False)

## e.
# Die Zahl 0 wird nicht zum durschnit dazu gezählt, da 0 das Programm beendet.
print("\nAufgabe 1e:")
print("Das Programm nimmt so lange Zahlen ein bis eine 0 eingegeben wird.")
counter = 0
mySum = 0
while True:
    userInput = input("Enter a number (or 0 to exit): ")
    try:
        num = int(userInput)
        if num == 0:
            break
    except ValueError:
        if userInput == "":
            print("You have to enter something.")
        elif userInput.isspace():
            print("Whitespace characters like spaces or tabs are not a valid input.")
        else:
            print("The entry has to be an integer.")
    else:
        counter += 1
        mySum += num
try:
    print(f"The sum is {mySum/counter}")
except ZeroDivisionError:
    print("You didn't enter any numbers.")

# Aufgabe 2
## a.
print("\nAufgabe 2a:")
print("Das Programm nimmt ein Alter ein und gibt den Preis für den Eintritt aus.")
age = input("How old are you? ")
try:
    age = int(age)
except ValueError:
        print("The entry has to be an integer.")
else:
    mySum = 10 if age < 12 else 12 if age <= 18 else 14 if age < 65 else 12
    print(f"Your ticket costs {mySum}.")

## b.
print("\nAufgabe 2b:")
print("Example von if-elif-else statements mit if-then statements ersetz.")
number = input("Enter a number: ")
try:
    number = int(number)
    if number == 1:
        print("One")
    if number == 2:
        print("Two")
    if number == 3:
        print("Three")
    if number > 3:
        print("Greater than three")
except ValueError:
    print("Please enter a valid integer!")

## c. do-while in python
"""
Bei der do-while Schleife steht der Ausführungblock vorgesetzt zur bedingung zur Terminierung. So wird, im Gegensatz
zur klassischen While-schleife, erst ausgeführt und dann die Bedingung überprüft.
"""
x = 0
while(True):
    print("Grüße aus der 'do'-Whileschleife")
    if(x <= 0):
        break
    else:
        x -=1

while(x<=0):
    print("Grüße aus der klassischen while-Schleife")

## d.
print("\nAufgabe 2d:")
print("Das Programm nimmt 3 ganze Zahlen an und gibt aus wie viele verschiedene Zahlen eingeben wurden.")
# Könnte man mit einem set lösen, da es keine doppelten Zahl animmt, aber es würde den Stoff sprengen.
myList = [] 
#userInput = input("Wie viele Zahlen möchtest du eingeben? ")
#try:
#    amount = int(userInput)
#except ValueError:
 #   print("The entry has to be an integer.")
 #   exit()
amount = 3
for i in range(amount):
    userInput = input(f"Enter a number: ")
    try:
        num = int(userInput)
    except ValueError:
        print("The entry has to be an integer.")
        exit()
    myList.append(num)

# zaehle die unterschiedlichen Zahlen, also erste anderes als zweite und dritte und zweite anderes als dritte
count = 0
length = len(myList)
for i in range(length):
    for j in range(i+1, length):
        if myList[i] != myList[j]:
            count += 1

print("Es gibt", count, "unterschiedliche Zahlen.")

## e.
print("\nAufgabe 2e:")
print("Das Programm gibt eine Pyramide aus, die so viele Zeilen hat wie der User eingibt.")
blank = " "

userInput = input("How many lines? ")
try:
    n = int(userInput)
except ValueError:
    print("Please enter a valid number!")
    exit()

for i in range(1, n+1):
    sequence = blank * (n - i)
    for j in range(i, 0, -1):    
        sequence += str(j)    
    for k in range(2, i+1):    
        sequence += str(k)  
    print(sequence)
# Aufgabe 3
## a.
print("\nAufgabe 3a:")
print("Das Programm gibt die durchschnittliche Anzahl an Schritte aus, die benötigt werden um bei einem Zufallsspaziergang eine bestimmte Anzahl an Schritten zu erreichen.")
import random

def randomWalk(target):
    z = 0
    stepCounter = 0

    while z != target:
        if z == 0:
            z += 1
        else:
            if random.randint(0, 1) == 0:
                z += 1
            else:
                z -= 1
        stepCounter += 1

    return stepCounter

def averageSteps(target, numOfTrials = 10000):
    totalSteps = sum(randomWalk(target) for i in range(numOfTrials))
    return totalSteps / numOfTrials

targets = [10, 20, 30, 40, 50]
for target in targets:
    print(f"Average steps to reach {target}: {averageSteps(target)}")

"""
Man kann die durschnittliche Anzahl der Schritte mit der Folgenden Formel ausrechnen: 
Schritte ~= Zahl^2
"""
