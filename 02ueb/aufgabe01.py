"""
Uebungsblatt 1
Autors: Julian Mueller, Marc Lambertz und David Glaser
Datum: 03.Nov 23
Beschreibung: In dieser Python File sind die Antworten für die Aufgaben 1.
"""

"""
Mit Zahlen können folgende Probleme auftreten:
    - Konversions Fehler: wenn man einen String in eine Zahl umwandeln will, aber der String keine Zahl ist
    - Division durch 0
    - Overflow: wenn die Zahl zu groß ist, um sie zu speichern. Passiert in Python nur mit floats, denn ints haben keine Obergrenze (außer der Speicherplatz)
    - Unterflow: wenn die Zahl zu klein ist, um sie zu speichern. Passiert in Python nur mit floats, denn ints haben keine Untergrenze (außer der Speicherplatz)
    - Rundungs Fehler: wenn man 0.1 + 0.2 rechnet ist das nicht 0.3
"""
### Aufgabe 1a
# Einteilung der einzelnen Lernziele nach den Lernzielen im whiteboard
'''
Aufgabe 1
b kdp5
c kdp2 kdp7
d kdp2 kdp7

Aufgabe 2
a kdp2 kdp7
b kdp2 kdp7
c kdp2 kdp7
d kdp2 kdp7

'''

#Aufgabe 1b
def aufgabe1b():
    print("\nDie Auswahlmöglichkeiten: \n"
        "1: Division mit 0\n"
        "2: Überlauf\n"
        "3: Rundungsfehler\n"
        "4: Unterlauf")
    user_choice_outer = input("Ihre Wahl: ")
    if user_choice_outer == "1":
        print("\nDie Auswahlmöglichkeiten:\n"
                "1: int\n"
                "2: float\n"
                "3: komplex")
        user_choice_inner = input("Was wählen Sie? ")
        if user_choice_inner == "1":
            try:
                print(1/0)
            except Exception as e:
                print(f"\033[91m[int-Fehler] {e}\033[0m")
        elif user_choice_inner == "2":
            try:
                print(1.0/0.0)
            except Exception as e:
                print(f"\033[91m[float-Fehler] {e}\033[0m")
        elif user_choice_inner == "3":
            try:
                print(1j/0j)
            except Exception as e:
                print(f"\033[91m[komplex-Fehler] {e}\033[0m")
    elif user_choice_outer == "2":
        x = 1.79e308
        y = x * 2
        print("Wir haben", x, "mit 2 multipliziert. Ergebnis:", y)
        print(f"\033[91mEin Überlauf ist aufgetreten.\033[0m")
    elif user_choice_outer == "3":
        x = 0.1
        y = 0.2
        z = 0.3
        verify_addition = x + y == z
        print("Wir haben", x, "und", y, "addiert und mit", z, "verglichen. Ergebnis:", verify_addition)
        print(f"\033[91mEin Rundungsfehler ist aufgetreten.\033[0m")
    elif user_choice_outer == "4":
        x = 1.0
        bufferValue = x
        while x > 0:
            x = x / 2.0
            print("x/2 =", x)
        print("Wir haben kontinuierlich", bufferValue, "durch 2 geteilt, bis das Ergebnis zu klein war, um genau dargestellt zu werden.")
        print(f"\033[91mEin Unterlauf ist aufgetreten.\033[0m")

def aufgabe1c():
    user_string = input("Geben Sie Ihren String ein: ")
    user_dict = {}
    for i in user_string:
        if i in user_dict:
            user_dict[i] += 1
        else:
            user_dict[i] = 1
    output_string = "Zeichenhäufigkeiten:", user_dict
    return output_string

def aufgabe1d():
    """
    Es wurden keine Checks für die Eingabe erstellt, da wir eine richtige Eingabe erwarten.
    """
    dna_string = input("Geben Sie die umzukehrende DNA-Sequenz ein: ")
    dna_string = dna_string.upper()
    reversed_dna_string = ""
    complement_dict = {"A": "T", "T": "A", "C": "G", "G": "C"}

    for i in dna_string:
        reversed_dna_string += complement_dict[i]
    output_string = "Umgekehrte DNA-Sequenz: " + reversed_dna_string 
    return output_string 

while(True):
    print("\nDie Auswahlmöglichkeiten:\n"
        "1: b)\n"
        "2: c)\n"
        "3: d)\n"
        "4: Beenden")
    userChoice = input("Welche Aufgabe möchten Sie ausführen: ")
    if userChoice == "1":
        aufgabe1b()
    elif userChoice == "2":
        print(aufgabe1c())
    elif userChoice == "3":
        print(aufgabe1d())
    elif userChoice == "4":
        break
    else:
        print("Ihre Wahl existiert nicht. Bitte geben Sie eine Zahl zwischen 1 und 4 ein.")


#Aufgabe 1c
histo = {}
input_str = input("Eingabe bitte: ")

for char in input_str:
    x = histo.get(char)
    if x == None:
        histo.update({char: 1})
    else:
        histo.update({char: x+1})
print(histo)


#Aufgabe 1d
dna_seq = input("DNA Sequenz eigeben:")
dna_comp = ""
for char in dna_seq:
    if(char == "A" or char == "a"):
        dna_comp = "T"+dna_comp
    elif(char =="T" or char == "t"):
        dna_comp = "A"+dna_comp
    elif(char == "C" or char == "c"):
        dna_comp = "G"+dna_comp
    elif(char == "G" or char == "g"):
        dna_comp = "C"+dna_comp
    else:
      print("The character",char,"is not a representation of a dna-base and will be ignored")
print(dna_comp)
