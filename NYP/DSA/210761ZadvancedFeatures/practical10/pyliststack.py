# Implementation of the Stack ADT using a Python list.
class Stack:
    # Creates an empty stack.
    def __init__(self):
        self._theItems = list()
    
    # Returns True if the stack is empty or False otherwise.
    def isEmpty(self):
        return len(self) == 0

    # Returns the number of items in the stack.
    def __len__ (self):
        return len(self._theItems)

    # Returns the top item on the stack without removing it.
    def peek(self):
        assert not self.isEmpty(), "Cannot peek at an empty stack"
        return self._theItems[-1]

    # Removes and returns the top item on the stack.
    def pop(self):
        assert not self.isEmpty(), "Cannot pop from an empty stack"
        return self._theItems.pop()
    
    # Push an item onto the top of the stack.
    def push(self, item):
        self._theItems.append(item)
    
    def evalute(self,expression):
        for i in reversed(expression):
            if i in '0123456789':
                self.push(i)
            else:
                op1=self.pop()
                op2=self.pop()
                result=self.cal(op1,op2,i)
                self.push(result)
        return self.pop()
    def cal(self,op1,op2,i):
        if i == '*':
            return int(op1)*int(op2)
        elif i == '/':
            return int(op1)/int(op2)
        elif i == '+':
            return int(op1)+int(op2)
        elif i == '-':
            return int(op1)-int(op2)
        elif i == '^':
            return int(op1)^int(op2)