# The recursive "in-place" implementation
def recQuickSort(theList, first, last, sortOrder):
    # Check the base case (range is trivially sorted)
    if first >= last:
        return
    else:
        # Partition the list and obtain the pivot position
        pos = partitionSeq(theList, first, last,sortOrder)
        # Repeat the process on the two sublists
        recQuickSort(theList, first, pos - 1,sortOrder)
        recQuickSort(theList, pos + 1, last,sortOrder)


# Partitions the list using the first key as the pivot
def partitionSeq(theList, first, last,sortOrder):
    # Save a copy of the pivot value.
    pivot = theList[first]  # first element of range is pivot

    # Find the pivot position and move the elements around it
    left = first + 1  # will scan rightward
    right = last  # will scan leftward
    while left <= right:
        # Scan until reaches value equal or larger than pivot (or right marker)
        if sortOrder == "A":
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
        elif sortOrder == "D":
            while left <= right and theList[left] > pivot:
                left += 1

            # Scan until reaches value equal or smaller than pivot (or left marker)

            while left <= right and theList[right] < pivot:
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
print("Sorting in ascending order:")
print('Input List:', list_of_numbers)
recQuickSort(list_of_numbers, 0, len(list_of_numbers)-1, "A")
print('Sorted List:', list_of_numbers)


list_of_numbers = [12, 7, 9, 24, 7, 29, 5, 3, 11, 7]
print("----------------------------")
print("Sorting in descending order:")
print('Input List:', list_of_numbers)
recQuickSort(list_of_numbers, 0, len(list_of_numbers)-1, "D")
print('Sorted List:', list_of_numbers)