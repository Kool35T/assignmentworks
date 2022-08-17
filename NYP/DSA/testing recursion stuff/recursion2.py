star = "*"

def pattern(n,i):
    if n == 1:
        return ''
    else:
        return f'{star}\n{str(star * i)}\n' + pattern(n-1, i+1)
def pat(n):
    if n == 1:
        print("*")
    else:
        pat(n-1)
        print(n * "*")
pat(3)