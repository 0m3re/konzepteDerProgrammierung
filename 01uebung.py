"""
Uebungsblatt 1
Autor: David Glaser
Datum: ---
Beschreibung: In dieser Python File sind die Antworten für die Aufgaben 1, 2 und 3 Teil a.
"""

# Aufgabe 1
## a.

a = int(input("Enter the length of the side of the triangle: "))
ha = int(input("Enter the heigth of the triangle: "))

flaecheDreieck = (a * ha)/2

print(f"The area of the triangle is {flaecheDreieck}.")

## b.
x = int(input("Enter a number for x: "))
y = int(input("Enter a number for y: "))
userInput = input("Enter the Operator of your choice (+, -, *, /): ")
if userInput == "+":
    print(f"the result is {x+y}")
elif userInput == "-": 
    print(f"the result is {x-y}")
elif userInput == "*": 
    print(f"the result is {x*y}")
elif userInput == "/": 
    print(f"the result is {x/y}")
else:
    print(f"The user input {userInput} is not a valid option.")

## c.
i= 1
n = 1000
while(i < n):
    print(i)
    i += 1

## d.
numberCount = 3
numList = []
for i in range(3):
    numList = []
    for i in range(3):
        try:
            userInput = int(input("Enter a number: "))
            numList.append(userInput)
        except ValueError:
            print("Please enter a valid integer!")

    if len(set(numList)) == len(numList):
        print(True)
    else:
        print(False)

    userInput = 0
    mySum = 0
    counter = 0
## e.
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
age = input("How old are you? ")
try:
    age = int(age)
except ValueError:
        print("The entry has to be an integer.")
else:
    mySum = 10 if age < 12 else 12 if age <= 18 else 14 if age < 65 else 12
    print(f"Your ticket costs {mySum}.")

## b.
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
x = 0
while x < 10:
    print("x:", x)
    x += 1

## d.
# Könnte man mit einem set lösen, da es keine doppelten Zahl animmt, aber es würde den Stoff sprengen.
myList = [] 
length = 3

for i in range(length):
    userInput = input("Enter a number: ")
    number = int(userInput)
    myList.append(number)

# zaehle die unterschiedlichen Zahlen, also erste anderes als zweite und dritte und zweite anderes als dritte
count = 0
for i in range(length):
    for j in range(i+1, length):
        if myList[i] != myList[j]:
            count += 1

print("Es gibt", count, "unterschiedliche Zahlen, naemlich", myList)

## e.
blank = " "

userInput = input("How many lines? ")
n = int(userInput)

for i in range(1, n+1):
    sequence = blank * (n - i)
    for j in range(i, 0, -1):    
        sequence += str(j)    
    for k in range(2, i+1):    
        sequence += str(k)  
    print(sequence)

# Aufgabe 3
## a.
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
