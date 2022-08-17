def sum_of_squares(n):
    sum = 0
    for x in range(1, n+1):
        if x/2 != int(x/2):
            sum = sum + (x**2)
    return sum


print(sum_of_squares(3))
