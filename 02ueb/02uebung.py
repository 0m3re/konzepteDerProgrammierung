"""
Uebungsblatt 1
Autors: Julian Mueller, Marc Lambertz und David Glaser
Datum: ---
Beschreibung: In dieser Python File sind die Antworten für die Aufgaben 1, 2 und 3 Teil a.
"""

# Aufgabe 1
# a)
# b)
"""
Mit Zahlen können folgende Probleme auftreten:
    - Konversions Fehler: wenn man einen String in eine Zahl umwandeln will, aber der String keine Zahl ist
    - Division durch 0
    - Overflow: wenn die Zahl zu groß ist, um sie zu speichern. Passiert in Python nur mit floats, denn ints haben keine Obergrenze (außer der Speicherplatz)
    - Unterflow: wenn die Zahl zu klein ist, um sie zu speichern. Passiert in Python nur mit floats, denn ints haben keine Untergrenze (außer der Speicherplatz)
    - Rundungs Fehler: wenn man 0.1 + 0.2 rechnet ist das nicht 0.3
"""
# Examples
while True:
    print("\nThe choices:\n"
            "1: Zahlenprobleme und Stringprobleme\n"
            "2: Mastermind\n"
            "3: Exit")
    userChoice = input("Which task do you want to do: ")
    if userChoice == "1":
        print("\nYou chose task 1 'Zahlenprobleme und Stringprobleme'")
        while True:
            print("\nThe choices:\n"
                    "1: a)\n"
                    "2: b)\n"
                    "3: c)\n"
                    "4: d)\n"
                    "5: Exit")
            userChoice = input("Which task do you want to do: ")
            if userChoice == "1":
                print("\nYou chose a)")
            elif userChoice == "2":
                print("\nYou chose b)")
                while True:
                    print("\nThe choices: \n"
                            "1: Division with 0\n"
                            "2: Overflow\n"
                            "3: Rounding Error\n"
                            "4; Underflow\n"
                            "5: Exit")
                    userChoice = input("Your choice: ")
                    if userChoice == "1":
                        while True:
                            print("\nThe choices:\n"
                                    "1: int\n"
                                    "2: float\n"
                                    "3: complex\n"
                                    "4: Exit")
                            userChoice = input("What do you chose? ")
                            if userChoice == "1":
                                try:
                                    print(1/0)
                                except Exception as e:
                                    print(f"\033[91m[int error] {e}\033[0m")
                            elif userChoice == "2":
                                try:
                                    print(1.0/0.0)
                                except Exception as e:
                                    print(f"\033[91m[float error] {e}\033[0m")
                            elif userChoice == "3":
                                try:
                                    print(1j/0j)
                                except Exception as e:
                                    print(f"\033[91m[complex error] {e}\033[0m")
                            elif userChoice == "4":
                                break
                    elif userChoice == "2":
                        x = 1.79e308
                        y = x * 2
                        print("We multiplied", x, "by 2. Result:", y)
                        print(f"\033[91mOverflow occurred.\033[0m")
                    elif userChoice == "3":
                        x = 0.1
                        y = 0.2
                        z = 0.3
                        verifyAddition = x + y == z
                        print("We added", x, "and", y, "and compared it to", z, " Result:", verifyAddition)
                        print(f"\033[91mA rounding error occurred.\033[0m")
                    elif userChoice == "4":
                        x = 1.0
                        bufferValue = x
                        while x > 0:
                            x = x / 2.0
                            print("x/2 =", x)
                        print("We continuously divided", bufferValue, "by 2 until the result was too close to zero to be represented accurately.")
                        print(f"\033[91mUnderflow occurred.\033[0m")
                    elif userChoice == "5":
                        break
                    else:
                        print("Your choice does not exist. Enter a number between 1 and 5.")
            elif userChoice == "3":
                print("\nYou chose c)")
                # c)
                # Ask if the order is important, because it would mean that we can't use a dict, or at list we have to add something
                userString = input("Enter your string: ")
                userDict = {}
                for i in userString:
                    userDict[i] += 1
                print("Character frequencies:", userDict)
            elif userChoice == "4":
                print("\nYou chose d)")
                # d)
                DNAString = input("Enter the DNA string that you want to reverse: ")
                DNAString = DNAString.upper()
                reverseBool = True
                reversedDNAString = ""
                complementDict = {"A": "T", "T": "A", "C": "G", "G": "C"}
                for i in DNAString:
                    if i not in {"A","C","G","T"}:
                        print("You entered an undefined characters!!!")
                        reverseBool = False
                        break
                    else:
                        reversedDNAString += complementDict[i]
                if reverseBool == True:
                    print("Reversed DNA string:", reversedDNAString)
            elif userChoice == "5":
                break
            else:
                print("Your choice does not exist. Enter a number between 1 and 5.")
    elif userChoice == "2":
        print("\nYou chose task 2 'Mastermind'")
        while True:
            print("\nThe choices:\n"
                    "1: a)\n"
                    "2: b)\n"
                    "3: c)\n"
                    "4: d)\n"
                    "5: Exit")
            userChoice = input("Which task do you want to do: ")
            if userChoice == "1":
                print("\nYou chose a)")
                # a)
                import random
                
                random.seed()
                choiceList = ["A","C","G","T"]
                randomDNAString = ""
                for i in range(6):
                    randomDNAString += random.choice(choiceList) 
                print("Randomly generated DNA string:", randomDNAString)
            elif userChoice == "2":
                print("\nYou chose b)")
                # b)
                DNAString1 = input("Enter the first DNA String: ")
                DNAString2 = input("Enter the second DNA String: ")
                if len(DNAString1) > 6 or len(DNAString2) > 6:
                    print("Both DNA strings should be 6 characters long.")
                else:
                    DNAString1 = DNAString1.upper()
                    DNAString2 = DNAString2.upper()
                    DNABool = True
                    for i in DNAString1:
                        if i not in {"A","C","G","T"}:
                            print("Invalid character detected. DNA string can only contain the letters A, C, G, and T.")
                            DNABool = False
                            break
                    for i in DNAString2:
                        if i not in {"A","C","G","T"}:
                            print("Invalid character detected. DNA string can only contain the letters A, C, G, and T.")
                            DNABool = False
                            break
                    if DNABool == True:
                        matchingCharacters = 0
                        if DNAString1 == DNAString2:
                            matchingCharacters = 6
                        else:
                            for i in range(6):
                                if DNAString1[i] == DNAString2[i]:
                                    matchingCharacters += 1
                        print("Number of matching characters:", matchingCharacters)
            elif userChoice == "3":
                print("\nYou chose c)")
                # c)
                DNAString1 = input("Enter the first DNA String: ")
                DNAString2 = input("Enter the second DNA String: ")
                if len(DNAString1) > 6 or len(DNAString2) > 6:
                    print("Both DNA strings should be 6 characters long.")
                else:
                    DNAString1 = DNAString1.upper()
                    DNAString2 = DNAString2.upper()
                    DNABool = True
                    for i in DNAString1:
                        if i not in {"A","C","G","T"}:
                            print("Invalid character detected. DNA string can only contain the letters A, C, G, and T.")
                            DNABool = False
                            break
                    for i in DNAString2:
                        if i not in {"A","C","G","T"}:
                            print("Invalid character detected. DNA string can only contain the letters A, C, G, and T.")
                            DNABool = False
                            break
                    if DNABool == True:
                        characterList = ["A","C","G","T"]
                        matchingCharactersList = [0,0,0,0]
                        for i in range(6):
                            for j in range(4):
                                if DNAString1[i] == characterList[j]:
                                    matchingCharactersList[j] += 1
                                if DNAString2[i] == characterList[j]:
                                    matchingCharactersList[j] += 1
                        counter = 0
                        for i in range(4):
                            if matchingCharactersList[i] % 2 == 0:
                                counter += 1 
                        print("The amount of matching characters counts:", counter)
            elif userChoice == "4":
                print("\nYou chose d)")
                # d)
                import random

                random.seed()
                choiceList = ["A","C","G","T"]
                randomDNAString = ""
                for i in range(6):
                    randomDNAString += random.choice(choiceList)
                userGuess = input("Enter your guess: ")
                if len(userGuess) > 6:
                    print("You entered a Guess that is longer than 6 characters.")
                else:
                    userGuess = userGuess.upper()
                    guessBool = True
                    for i in userGuess:
                        if i not in {"A","C","G","T"}:
                            print("You entered an undefined characters.")
                            guessBool = False
                            break
                    if guessBool == True:
                        if randomDNAString == userGuess:
                            print("You won. You guessed the correct DNA string.")
                        else:
                            matchingCharactersList = [0,0,0,0]
                            for i in range(6):
                                for j in range(4):
                                    if DNAString1[i] == characterList[j]:
                                        matchingCharactersList[j] += 1
                                    if DNAString2[i] == characterList[j]:
                                        matchingCharactersList[j] += 1
                            counter = 0
                            for i in range(4):
                                if matchingCharactersList[i] % 2 == 0:
                                    counter += 1 
                            print("From the available characters (A,C,T,G),", counter, "are in the right amount.")
                            matchingCharacters = 0
                            for i in range(6):
                                if randomDNAString[i] == userGuess[i]:
                                    matchingCharacters += 1
                            print("The amount of characters at the right position is", counter)
            elif userChoice == "5":
                break
    elif userChoice == "3":
        exit()
    else:
        print("You're choice does not exist.")
