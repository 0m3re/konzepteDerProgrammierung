"""
Uebungsblatt 2
Autors: Julian Mueller, Marc Lambertz und David Glaser
Datum: 03.Nov 23
Beschreibung: In dieser Python File sind die Antworten für die Aufgaben 2a-d
"""

import random
random.seed()
## Die Einzlenen Funktionen sind jeweils das Ergebnis der Teilaufgaben von 2a-c

## Aufgabe 2a - sechstellige Basensequenz als string.
## () -> str // Erzeugt sechstellige Basensequenz als str und gibt diese zurück.
def create_base_list():
    dna_str = ""
    i = 6
    while(i>0):
        x = random.randint(1,4)
        if x==1:
            dna_str += "A"
        if x==2:
            dna_str += "C"
        if x==3:
            dna_str += "G"
        if x==4:
            dna_str += "T"
        i-=1

    """
    dna_list = ["A","C","G","T"]
    dna_str = ""
    for i in range(6):
        dna_str += random.choice(dna_list) 
    """
    return dna_str


## Aufgabe 2b - Positionaler Vergleich der Einzelnen Basen. Returned integer der Anzahl der gleichen Stellen
## (str, str) -> int // Gibt die Anzahl der gleichen Positionen in den jeweiligen str zurück.
def compare_position(base_str_a, base_str_b):
    same_position = 0
    base_str_a = base_str_a.upper()
    base_str_b = base_str_b.upper()
    
    if(base_str_a == base_str_b):
        same_position = 6
    else:
        for i in range(6):
            if(base_str_a[i] == base_str_b[i]):
                same_position +=1
    return same_position

## Aufgabe 2c - Vergleich der Häufigkeit in den einzelen Basen
## base_prec(str) -> {} // String returned Häufigkeitsverteilung einzelnen chars als Dict.
## compare_prev(str, str) -> int // Vergleich der Häufigkeitsverteilung (base_prec()) zweier Strings.
def base_prev(base_str):
    histo = {}
    for char in base_str:
        x = histo.get(char)
        if x == None:
            histo.update({char: 1})
        else:
            histo.update({char: x+1})
    return histo

def compare_prev(base_str_a, base_str_b):
    first_prev = base_prev(base_str_a)
    second_prev = base_prev(base_str_b)
    prev = 0
    for key, prevalence in first_prev.items():
        if second_prev.get(key) == prevalence:
            prev+=1
    return prev


## Aufgabe 2d - Zusammenführung der vorheringen Aufgaben.
## 
print('Willkommen beim Base-Sequenzen-Raten - total spannend.')
base_sequenz = create_base_list()
rounds = []
prevalence = 0
position = 0


while(True):
    if(len(rounds)<1):
        print("Runde 1! Bitte mache deine erste Eingabe!")
    else:
        print("Runde",len(rounds)+1,"-", "Deine Eingabe in der Letzten Runde war:",rounds[len(rounds)-1],"Dabei waren", position,"korrekte Positionen und mit", prevalence,"gleicher Häufigkeit!")
    round_input = str.upper(input("Bitte sechstellige Basensequenz eingeben:"))
    position = compare_position(base_sequenz, round_input)
    if(position == 6):
        print("RICHTIG!! die gesuchte Basensequenz war:", round_input)
        break
    else:
        prevalence = compare_prev(base_sequenz, round_input)
        rounds.append(round_input)
