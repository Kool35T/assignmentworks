def sumDigits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sumDigits(int(n/10))

# Test code
print(sumDigits(368))