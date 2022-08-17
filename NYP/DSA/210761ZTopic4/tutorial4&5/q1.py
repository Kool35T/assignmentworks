# Qn 1a
# Sorts a sequence in ascending order using the
# optimized bubble sort algorithm
def bubbleSort_optimized(theSeq):
    n = len(theSeq)
    
    # Perform n-1 bubble operations on the sequence
    for i in range(n - 1, 0, -1):
        print(theSeq)
        # Set boolean variable to check occurrence of swapping
        # in inner loop
        noSwap = True
        
        # Bubble the largest item to the end
        for j in range(i):
            if theSeq[j] > theSeq[j + 1]:
                # Swap the j and j+1 items
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp
                
                # Set boolean variable value if swapping occurred
                noSwap = False
                
        # Exit the loop if no swapping occurred
        # in the previous pass
        if noSwap:
            break
        
# Test code
data = [1,2,3,5,4]
bubbleSort_optimized(data)

# Qn 1b - Solution
# Using standard Bubble Sort, 4 passes are required.
# Using optimized Bubble Sort, 2 passes are required.

# Qn 1c - Solution
# Using optimized Bubble Sort to sort an already sorted list, only 1 pass is required.
# One advantage that Bubble Sort has over other sorting algorithms is having
# an efficient way to check if a list of numbers is already sorted in order.
