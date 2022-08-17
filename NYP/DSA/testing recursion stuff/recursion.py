# pattern(0)
# 0
# pattern(1)
# 0 1 0
# pattern(2)
# 0 1 0 2 0 1 0
# pattern(3)
# 0 1 0 2 0 1 0 3 0 1 0 2 0 1 0
# pattern(4)
# 0 1 0 2 0 1 0 3 0 1 0 4 0 1 0 3 0 1 0 2 0 1 0

def pattern(n):
    if n == 0:
        print("0", end=" ")
        return n
    else: 
        pattern(n-1)
        print(n, end=" ")
        pattern(n-1)
    
pattern(4)