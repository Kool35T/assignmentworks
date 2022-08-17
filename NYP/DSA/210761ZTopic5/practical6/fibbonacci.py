def fib(n):
    assert n >= 0, "Fibonacci not defined for n < 0"

    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n-2)


for i in range(4):
    print(fib(i), end=' ')
