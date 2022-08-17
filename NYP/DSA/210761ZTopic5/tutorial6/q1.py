def main():
    # Compute and print the sum of (1 + 2 + ... + 10)
    print(sum(10))
    
def sum(x):
    # Assuming x >= 1
    # Complete this function recursively
    if x == 1: # Base case
        return 1
    else: # Recursive case
        return x + sum(x-1) # Progresses towrds base case

main()