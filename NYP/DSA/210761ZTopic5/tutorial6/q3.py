def main():
    y = foo(4)
    bar(2)
    
def foo(x):
    if x % 2 != 0:
        return 0
    else:
        return x + foo(x-1)
    
def bar(n):
    if n > 0:
        bar(n-1)
        print(n)
        
main()
