def binarySearch(theValues, target):
    #start with the entire sequence of elements
    low = 0
    high = len(theValues) -1

    #Repeatedly subdivide the sequence in half
    #until the target is found
    while low <= high:
        #Find the midpoint of the squence 
        mid = (high +low )//2

        #does the midpoint contain the target?
        #if yes, return midpoint(i.e. index of the list)
        if theValues[mid] == target:
            return mid
        #or is the target before the midpoint?
        elif target < theValues[mid]:
            high = mid - 1
        #or is the target after the midpoint?
        else:
            low = mid + 1

    #if the sequence cannot be subdivided further,
    #target is not in the list of values

    return -1

#test code
sortedListofNum = [1, 2, 7, 10, 18, 25, 30, 33, 42, 56, 61, 70, 73, 88]
print(binarySearch(sortedListofNum, 10))
print(binarySearch(sortedListofNum, 73))
print(binarySearch(sortedListofNum, 12))