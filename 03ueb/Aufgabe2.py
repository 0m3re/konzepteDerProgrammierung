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
