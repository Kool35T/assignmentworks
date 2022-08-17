def recbinarySearch(target, theValues, first, last):
    if first > last:
        return False
    else:
        # find the midpoint of the sequence
        mid = (last + first) // 2

        # does the element at the midpoint contain the target?
        if theValues[mid] == target:
            return True  # Base Case #2
        # or does the target precede the element at the midpoint
        elif target < theValues[mid]:
            return recbinarySearch(target, theValues, first, mid - 1)
        # or does the target follow the element at the midpoint
        else:
            return recbinarySearch(target, theValues, mid + 1, last)


# test code
sortedListofNum = [1, 2, 7, 10, 18, 25, 30, 33, 42, 56, 61, 70, 73, 88]
print(recbinarySearch(10, sortedListofNum, 0, len(sortedListofNum)))
print(recbinarySearch(73, sortedListofNum, 0, len(sortedListofNum)))
print(recbinarySearch(12, sortedListofNum, 0, len(sortedListofNum)))
