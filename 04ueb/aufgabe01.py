
# mergesort(List[U]) : NoneType # U is an arbitrary type
# Precondition: The elements of xs are from a totally ordered universe.
# Effect: The elements of xs are sorted in increasing order.
# Result: None
'''Tests: Your exercise ;-)'''
def mergesort(xs):
    n = len(xs)
    if n <= 1: # recursion anchor
        return
    # take a copy of the left and right half of xs
    # (This corresponds to the lower part of the figure from above.)
    left = xs[:n//2]
    right = xs[n//2:]
    print("first left:", left)
    print("first right:", right)
    print("first xs:", xs)
    # sort the two copies recursively ...
    mergesort(left)
    mergesort(right)
    # ... and merge them back into the original list xs
    # (This corresponds to the upper part of the figure from above)
    merge(left, right, xs)

# merge(List[U], List[U], List[U]) : NoneType # U is an arbitrary type
# Precondition: len(left) + len(right) == len(xs), left and right are sorted inc.
# Result: None
# Effect: The elements of left and right are in xs sorted increasingly.
'''Tests: Your exercise ;-)'''
def merge(left, right, xs):
    print("merge aufgerufen")
    # l is the index of the first element of left, that has not been copied to xs
    # r is the index of the first element of right, that has not been copied to xs
    l = 0
    r = 0
    print("before left:", left)
    print("before right:", right)
    print("before xs:", xs)
    while l + r < len(xs):
        if l == len(left): # No more elements in left
            xs[l + r] = right[r]
            r += 1
        elif r == len(right): # No more elements in right
            xs[l + r] = left[l]
            l += 1
        elif left[l] <= right[r]: # In left is the smaller element
            xs[l + r] = left[l]
            l += 1
        else: # left[l] > right[r] # In right is the smaller element
            xs[l + r] = right[r]
            r += 1
        print("while left:", left)
        print("while right:", right)
        print("while xs:", xs)

mergesort([13, 42, 9, 0, 17, 35, 42, 10, 6, 15, 56, 7, 8])

# binary_search_first_greater(List[U], T) : NoneType # U and T are an arbitrary type
# Precondition: The elements of xs are ints and xs is sorted in increasing order.
# Effect: Find the smallest index i in xs such that k < xs[i]
# Result: None
def binaersuche(xs, k):
    left, right = 0, len(xs) - 1
    result = len(xs)  # Standardwert, falls kein Element > k gefunden wird

    while left <= right:
        mid = (left + right) // 2
        if xs[mid] > k:
            result = mid  # Ein Kandidat gefunden, aber es könnte noch einen kleineren Index geben
            right = mid - 1
        else:
            left = mid + 1

print(binaersuche([1, 2, 3, 4, 5, 6, 7, 9, 100], 8))

def binaersuche(xs, left, right, key):
    while left < right:
        mid = (left + right) // 2
        if xs[mid] < key:
            left = mid + 1
        else:
            right = mid
    return left

def insert(xs, i):
    key = xs[i]
    # Finde die richtige Position für den key mit Binärsuche
    pos = binaersuche(xs, 0, i, key)

    # Verschiebe alle Elemente nach rechts, um Platz für den key zu schaffen
    for j in range(i, pos, -1):
        xs[j] = xs[j - 1]

    # Füge key an der gefundenen Position ein
    xs[pos] = key

def insertion_sort(xs):
    n = len(xs)
    for i in range(1, n):
        insert(xs, i)

def merge_three_lists(list1, list2, list3):
    merged = []
    i, j, k = 0, 0, 0

    while i < len(list1) and j < len(list2) and k < len(list3):
        min_value = min(list1[i], list2[j], list3[k])
        if min_value == list1[i]:
            merged.append(list1[i])
            i += 1
        elif min_value == list2[j]:
            merged.append(list2[j])
            j += 1
        else:
            merged.append(list3[k])
            k += 1

    # Füge restliche Elemente hinzu
    for lst, index in [(list1, i), (list2, j), (list3, k)]:
        while index < len(lst):
            merged.append(lst[index])
            index += 1

    return merged

def powersort(xs):
    if len(xs) <= 1:
        return xs

    # Teile die Liste in drei nahezu gleich große Teile
    third = len(xs) // 3
    first_part = xs[:third]
    second_part = xs[third:2*third]
    third_part = xs[2*third:]

    # Sortiere die erste und dritte Teilliste mit Insertionsort
    insertion_sort(first_part)
    insertion_sort(third_part)

    # Rekursives Sortieren der zweiten Teilliste mit Powersort
    second_part_sorted = powersort(second_part)

    # Führe alle drei sortierten Teillisten zusammen
    return merge_three_lists(first_part, second_part_sorted, third_part)

