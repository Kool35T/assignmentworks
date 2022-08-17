def sum_of_squares(n):
    sum = 0
    for x in range(n+1):
        sum = sum + (x**2)
    return sum

print(sum_of_squares(3))
