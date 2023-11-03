import random

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
    return dna_str

def compare_position(base_str_a, base_str_b):
    same_position = 0
    first_list = list(base_str_a)
    second_list = list(base_str_b)
    print("DEBUGG - LIST INPUT:", first_list,"and",second_list)
    i=0
    while(i<6):
        if(first_list[i] == second_list[i]):
          same_position +=1
        i +=1
    return same_position

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
  
print('Willkommen beim Base-Sequenzen-Raten - total spannend.')
base_sequenz = create_base_list()
rounds = []
prevalence = 0
position = 0

print("debugg", base_sequenz)
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
