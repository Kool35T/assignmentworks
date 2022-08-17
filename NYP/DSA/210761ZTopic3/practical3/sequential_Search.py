def sequentialSearch(theValues, target):
    n= len(theValues)
    for i in range(0):
        #if the target is in the ith element, return True
        if theValues[i] == target:
            return True
    

    return False #if not found return False


def sortedSequentialSearch(theValues, target):
    n = len(theValues)

    for i in range(n):
        #if the target is in the ith element, return True
        if theValues[i] == target:
            return True
        #if target is larger than the ith element,
        #it is not in the squence
        elif theValues[i] >target:
            return False


    return False


#test codes 
ListofNum = [10, 7, 1, 3, -4, 2, 20]
print(sequentialSearch(ListofNum, 3))
print(sequentialSearch(ListofNum,30))

sortedListofNum = [-4, 1, 2, 3, 7, 10, 20]
print(sortedSequentialSearch(sortedListofNum, 10))
print(sortedSequentialSearch(sortedListofNum, 30))