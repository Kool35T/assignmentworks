import pyliststack as stack

def transfer(S, T):
    while not S.isEmpty():
        T.push(S.pop())
        
# Test code
S = stack.Stack()
T = stack.Stack()

for i in range(10,60,10):
    S.push(i)
    
print('Before')
print('S: ', S)
print('T: ', T)

transfer(S, T)

print('After')
print('S: ', S)
print('T: ', T)