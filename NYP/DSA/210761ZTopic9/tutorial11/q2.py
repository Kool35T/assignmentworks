import pylistqueue as queue
import pyliststack as stack

def reverseQueue(Q):
    S = stack.Stack()
    while not Q.isEmpty():
        S.push(Q.dequeue())
    while not S.isEmpty():
        Q.enqueue(S.pop())
        
# Test code
myQueue = queue.Queue()

for i in range(10,60,10):
    myQueue.enqueue(i)
    
print('The contents of the queue (BEFORE REVERSING):')
print(myQueue)

reverseQueue(myQueue)

print('\nThe contents of the queue (AFTER REVERSING):')
print(myQueue)