# Sorts a Python list in ascending order using the quick sort
# algorithm
def quickSort(theList):
    n = len(theList)
    recQuickSort(theList, 0, n-1)


# The recursive "in-place" implementation
def recQuickSort(theList, first, last):
    # Check the base case (range is trivially sorted)
    if first >= last:
        return
    else:
        # Partition the list and obtain the pivot position
        pos = partitionSeq(theList, first, last)
        # Repeat the process on the two sublists
        recQuickSort(theList, first, pos - 1)
        recQuickSort(theList, pos + 1, last)


# Partitions the list using the first key as the pivot
def partitionSeq(theList, first, last):
    # Save a copy of the pivot value.
    pivot = theList[first]  # first element of range is pivot

    # Find the pivot position and move the elements around it
    left = first + 1  # will scan rightward
    right = last  # will scan leftward
    while left <= right:
        # Scan until reaches value equal or larger than pivot (or right marker)
        while left <= right and theList[left] < pivot:
            left += 1

        # Scan until reaches value equal or smaller than pivot (or left marker)
        while left <= right and theList[right] > pivot:
            right -= 1

        # Scans did not strictly cross
        if left <= right:
            # swap values
            theList[left], theList[right] = theList[right], theList[left]
            # Shrink range (Recursion: Progress towards base case)
            left += 1
            right -= 1

    # Put the pivot in the proper position (marked by the right index)
    theList[first], theList[right] = theList[right], pivot
    # Return the index position of the pivot value.
    return right


# Test code
list_of_numbers = [12, 7, 9, 24, 7, 29, 5, 3, 11, 7]
print('Input List:', list_of_numbers)
quickSort(list_of_numbers)
print('Sorted List:', list_of_numbers)
