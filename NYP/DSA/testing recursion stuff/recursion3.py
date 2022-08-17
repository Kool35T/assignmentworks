def foo(n):
    if n <= 2:
        return n
    else:
        return foo(n-1) + foo(n-2) + foo(n-3)

print(foo(5))