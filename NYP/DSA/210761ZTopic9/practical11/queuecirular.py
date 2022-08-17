# Implementation of the Queue ADT using a circular array.
from msilib import MSIMODIFY_ASSIGN


class Queue:
    # Creates an empty queue.
    def __init__(self, maxSize):
        self._count = 0
        self._front = 0
        self._back = maxSize - 1
        self._qArray = [None] * maxSize
    # Returns True if the queue is empty.

    def isEmpty(self):
        return self._count == 0

    # Returns True if the queue is full.
    def isFull(self):
        return self._count == len(self._qArray)
    # Returns the number of items in the queue.

    def __len__(self):
        return self._count
    # Adds the given item to the queue.

    def enqueue(self, item):
        assert not self.isFull(), "Cannot enqueue to a full queue."
        maxSize = len(self._qArray)
        self._back = (self._back + 1) % maxSize
        self._qArray[self._back] = item
        self._count += 1
    # Removes and returns the first item in the queue.

    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."
        item = self._qArray[self._front]
        maxSize = len(self._qArray)
        self._front = (self._front + 1) % maxSize
        self._count -= 1
        return item
    # Return the content of the queue (with array index in square brackets].

    def __str__(self):
        maxSize = len(self._qArray)
        outStr = ''
        for i in range(self._count):
            outStr += ('[' + str((self._front + i) % maxSize) + ']:')
            outStr += (str(self._qArray[(self._front + i) % maxSize]) + ' ')
        return outStr


if __name__ == '__main__':

    myQueue = Queue(5)
    myQueue.enqueue(10)
    myQueue.enqueue(20)
    myQueue.enqueue(30)
    myQueue.enqueue(40)
    myQueue.enqueue(50)
    print("Testing with a queue of maximum size of 5 items")
    print("After enqueuing 5 items to an empty queue: ")
    print(myQueue)

    myQueue.dequeue()
    myQueue.dequeue()
    print("\nAfter dequeuing 2 items from the queue:")
    print(myQueue)

    myQueue.enqueue(60)
    myQueue.enqueue(70)
    print("\nAfter enqueuing 2 more items to the queue")
    print(myQueue)
