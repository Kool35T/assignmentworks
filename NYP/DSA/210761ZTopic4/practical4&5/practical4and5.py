# q1
def selectionSort(theSeq, sortOrder): 
    n = len(theSeq)
    for i in range(n - 1):
        smallNdx = i
        for j in range(i + 1, n):

            if theSeq[j] < theSeq[smallNdx] and sortOrder == "A":
                smallNdx = j
            elif theSeq[j] > theSeq[smallNdx] and sortOrder == "D":
                smallNdx = j
        if smallNdx != i:
            theSeq[i], theSeq[smallNdx] = theSeq[smallNdx], theSeq[i]
    return theSeq

list_of_numbers = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]

print("Sorting in ascending order:")
print('Input List:', list_of_numbers)
selectionSort(list_of_numbers, sortOrder="A")
print('Sorted List:', list_of_numbers)

list_of_numbers = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
print("-----------------------------")
print("Sorting in descending order:")
print('Input List:', list_of_numbers)
selectionSort(list_of_numbers, sortOrder="D")
print('Sorted List:', list_of_numbers)

# q2
def insertionSort(theSeq):
    n = len(theSeq)
    pass_ = 0
    for i in range(1, n):
        value = theSeq[i]
        pos = i
        while pos > 0 and value < theSeq[pos - 1]:
            theSeq[pos] = theSeq[pos - 1]
            pos -= 1
        theSeq[pos] = value
        pass_ += 1


list_of_numbers = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
print("-----------------------------")
print("Insertion Sort:")
print('Input List:', list_of_numbers)
insertionSort(list_of_numbers)
print('Sorted List:', list_of_numbers)

# 3
print("-----------------------------")
l = ["Bougainvillea", "Orchids", "Hibiscus", "Frangipani", "Honeysuckle"]
print(sorted([x for x in l if x[0].upper() == "H"]) + sorted([x for x in l if x[0].upper() != "H"]))
print("-----------------------------")
b = [(1, 7), (1, 3), (3, 4, 5), (2, 2)]
print(list(sorted(b, key=lambda b: b[-1])))