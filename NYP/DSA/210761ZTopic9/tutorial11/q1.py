# Qn 1a
myQueue = Queue()
for i in range(16):
    if i % 3 == 0:
        myQueue.enqueue(i)

# Qn 1b        
myQueue = Queue()
for i in range(16):
    if i % 3 == 0:
        myQueue.enqueue(i)
    elif i % 4 == 0:
        myQueue.dequeue()

# Qn 1c     
myQueue = Queue()
for i in range( 16 ):
    if i % 3 == 0:
        myQueue.enqueue(i)
        myQueue.enqueue(i + 1)
    elif i % 4 == 0:
        myQueue.dequeue()
        
# Qn 1d
myQueue = Queue()
for i in range( 16 ):
    if i % 4 == 0:
        myQueue.dequeue()
    elif i % 3 == 0:
        myQueue.enqueue(i)
