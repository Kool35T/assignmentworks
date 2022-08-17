import pyliststack as stack

def recEmptyStack(S):
    if S.isEmpty():
        return S
    else:
        S.pop()
        recEmptyStack(S)
        
# Test code
S = stack.Stack()

for i in range(10, 60, 10):
    S.push(i)
    
print('Before')
print('S: ', S)

recEmptyStack(S)

print('After')
print('S: ', S)

