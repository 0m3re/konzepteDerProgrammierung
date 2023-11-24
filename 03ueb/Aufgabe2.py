###
### Aufgabe 2 - a
###
### Etwas clunky das Ganze. Das geht sicher kürzer.

#binarysearch(List[int], int):Bool
#Precondition: A non empty list that is sorted in ascending order
#Effect: None
#Result: Returns true/false if list contains the int-element or dosent.
''' Test cases:
binarysearch(search_list, 16) == True
binarysearch(search_list, 1621) == False

'''
search_list = [289,244,243,130,128,64,42,32,16,8,4,2,1]
import math
search_list.sort()

def bsearch(s_list, num):
    print("Liste:",s_list)
    length = len(s_list)
    #Ich bin mal mutig und nehme an, dass das typcasting hier einfach abrundet.. ansonsten halt math.floor()
    mid = int(length/2)
    #Wir haben 4 Fälle:
    # 1. wenn s_list[mid] == der gesuchten nummer ist brechen wir mir true ab.
    # 2. wenn die Liste <2 also maximal nur ein Element beinhaltet und nicht der erste Fall eingetreten ist ist das Element nicht in der Liste, daher Rückgabe False
    # 3. Wenn also mehr als ein Element in der Liste ist vergleichen wir das Element mit dem Index len(list)/2 = mid mit unserer gesuchten Nummer, hier wird bei größer der linke Teil der liste übergeben
    # 4. Analog zu 3. hier nur falls das mid-element kleiner ist als das Gesuchte
    
    #wir haben hier noch den Fall, dass die Zahl größer oder kleiner ist als das jeweils größte/kleinste Element der Liste. Dies führt auch zum kompletten durchlauf und wäre, unter der Bedingung
    #dass die Liste sortiert wäre vorher einfach zu prüfen um eine Berechnung über lange Listen zu verhindern. Ich würde hier wahrscheinlich einfach vorher die Sortierung überprüfen und die jeweiligen max/min. 
    if length <2:
        if length == 0:
            return False
        elif s_list[0] == num:
            return True
        else:
            return False
    elif s_list[mid] == num:
        return True
    elif s_list[mid]>num:
        print("Das gesuchte Element", num, "ist kleiner als das mid-Element:", s_list[mid])
        return bsearch(s_list[:mid],num)
    elif s_list[mid]<num:
        print("Das gesuchte Element", num, "ist größer als das mid-Element:", s_list[mid])
        return bsearch(s_list[mid+1:],num)
print("BESEARCH SHORT VERSION:")
print(bsearch(search_list, 1000))
print("----------------------------")


def binarysearch(s_list, num):
    print(s_list)
    list_length = len(s_list)
    if(list_length<2 and s_list[0]==num):
        return True
    elif(list_length<2):
        return False
    else:
        if(list_length%2 == 0):
            if(s_list[int(list_length/2)-1]>num):
                print("Debug- Gerade // s_list durchschnitt > num - calling binarysearch")
                return binarysearch(s_list[:list_length-1],num)
            elif(s_list[int(list_length/2)]<num):
                #Hier könnte noch ein zusätzliche Abbruchbedingung schreiben falls nummer größer ist als das größte Element der Liste um einen Aufruf zu sparen
                print("Debug- Gerade // s_list durchschnitt < num - calling binarysearch")
                return binarysearch(s_list[int(list_length/2):],num)
            #Dieser case cann nicht erreicht werden da die beiden ersten bereits beides abfangen.
            elif(s_list[int(list_length/2)-1]==num or s_list[int(list_length/2)]==num):
                return True
            else:
                return False
        else:
            if(s_list[math.floor(list_length/2)]>num):
                print("Debug- Ungerage // s_list durchschnitt > num - calling binarysearch")
                return binarysearch(s_list[:int(math.floor(list_length/2))],num)
            elif(s_list[math.floor(list_length/2)]<num):
                print("Debug- Ungerade // s_list durchschnitt < num - calling binarysearch")
                return binarysearch(s_list[int(math.floor(list_length/2)):],num)
            elif(s_list[math.floor(list_length/2)] == num):
                return True
            else:
                return False
              
print(binarysearch(search_list, 1621))

search_list = [289,244,243,130,128,64,42,32,16,8,4,2,1]
search_list.sort()

def bsearch(s_list, num):
    s_list.sort()
    if s_list[0]>num:
        return False
    elif s_list[len(s_list)-1]<num:
        return False
    else:
        return bsearch_calc(s_list, num)
    
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
      
print(bsearch_calc(search_list, 0))

###
### Aufgabe 2 - d
###

# smallest(List[Number])
# Precondition: Non empty list; Number of type int or float
# Effect: Everything but the smallest number will be deleted removed from the list
# Result: None
''' Test cases:
smallest([1,2,3,6,98,0]) == 0
smallest([9,827,1,3,5,7,1]) == 1
smallest([1]) == 1
smallest([1.0,1.3.0.3.10.5]) == 0.3
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
        
# k_smallest(List[Number]):Number
# Precondition: Non empty list; Number of type int or float
# Effect: None
# Result: The smallest number in a List of numbers is returned
''' Test cases

'''
def k_smallest(num_list):
    # Abbruchsbedingung für Liste < 2.
    if len(num_list)<2:
        return num_list[0]
    # Vergleich der jeweils ersten beiden Elemente der List - Rekurssion mit geslicter liste um das Listenobjekt nicht zu verändern
    elif num_list[0] < num_list[1]:
        return smallest(num_list[:1]+num_list[2:])
    else:
        return smallest(num_list[1:])


int_list = [10,103,9,82,33,21]
int_test_result = k_smallest(int_list)
print("Test mit int:", int_test_result, "mit dem Typ:", type(int_test_result))
print("Int - list looks like this:", int_list)
float_list = [10.2,10.3,0.9,8,33.3,21.1]
float_test_result = smallest(float_list)
print("Test mit float:", float_test_result, "mit dem Typ:", type(float_test_result))
print("float test:", float_list)

###
### Aufgabe 2 - e
###

# quersumme(int):float
# Precondition: None
# Effect: None
# Result: Returns the cross sum of the given Number
''' Test cases:

'''
def quersumme(num):
    x = num
    if x < 10:
        return x
    else:
        return (x% 10) + quersumme((x - (x % 10))/10)
      
print(quersumme(int(input("quersumme:"))))
