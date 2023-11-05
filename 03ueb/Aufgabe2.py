###
### Aufgabe 2 - d
###

# smallest(List[Number]):Number
# Precondition: Non empty list; Number of type int or float
# Effect: None                                                       !!!!!!! Muss hier die Kürzung der Liste hin?
# Result: The smallest number in a List of numbers is returned
''' Test cases:
smallest([1,2,3,6,98,0]) == 0
smallest([9,827,1,3,5,7,1]) == 1
smallest([1]) == 1
smallest([1.0,1.3.0.3.10.5]) == 0.3
'''

def smallest(num_list):
    # Abbruchsbedingung für Liste < 2.
    if len(num_list)<2:
        return num_list[0]
    # Vergleich der jeweils ersten beiden Elemente der List - das größere wird entfernt.
    elif num_list[0] < num_list[1]:
        del num_list[1]
        return smallest(num_list)
    else:
        del num_list[0]
        return smallest(num_list)

int_test_result = smallest([10,103,9,82,33,21])
print("Test mit int:", int_test_result, "mit dem Typ:", type(int_test_result))
float_test_result = smallest([10.2,10.3,0.9,8,33.3,21.1])
print("Test mit float:", float_test_result, "mit dem Typ:", type(float_test_result))
