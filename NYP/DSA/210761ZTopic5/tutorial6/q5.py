# q5a
def exp(x, n):
    y = 1
    for i in range(n):
        y *= x
    return y

print(exp(2,8))

# q5b
def exp_recursive(x, n):
    if n == 0:
        return 1
    else:
        return x * exp_recursive(x, n-1)
    
print(exp_recursive(2,8))