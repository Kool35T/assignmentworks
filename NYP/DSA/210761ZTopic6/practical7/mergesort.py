# sorts a python list in ascending order using the merge sort algorithm
from turtle import right


def mergesort(theList):
    # check the base case - the list contains a single item
    if len(theList) <= 1:
        return theList
    else:
        # compute the midpoint
        mid = len(theList) // 2

        # split the list and perform recursive step
        lefthalf = mergesort(theList[:mid])
        righthalf = mergesort(theList[mid:])

        # merge the two sorted sublists
        newList = mergesortedList(lefthalf, righthalf)
        return newList

# merge the two sorted lists to create and return a new sorted list


def mergesortedList(listA, listB):
    # create the new list and initialise the list markers
    newList = list()
    a = 0
    b = 0

    # merge the two lists together until one is empty
    while a < len(listA) and b < len(listB):
        if listA[a] < listB[b]:
            newList.append(listA[a])
            a += 1
        else:
            newList.append(listB[b])
            b += 1

    # if lista contains more items, append remaining items to newlist
    while a < len(listA):
        newList.append(listA[a])
        a += 1
    # if listb contains more items, append remaining items to newlist
    while b < len(listB):
        newList.append(listB[b])
        b += 1

    return newList


# test code
list_of_numbers = [12, 7, 9, 24, 7, 29, 5, 3, 11, 7]

print('Input List:', list_of_numbers)
merge_list = mergesort(list_of_numbers)
print('Sorted List:', merge_list)
