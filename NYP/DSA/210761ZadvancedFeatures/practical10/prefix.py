# Import the Stack implementation from Qn 1
import pyliststack as stack

print('prefix Expression Evaluator')
print('For help, type \"help\" or \"?\"')
print('To quit, type \"quit\" or \"q\"')

while True:
    expression = input("\nEnter a prefix expression to be evaluated: ")
    tokens = expression.split(" ") # Split the expression into individual tokens separated by space
    myStack = stack.Stack() # Create an instance of the Stack object
    
    # Handle help option
    if tokens[0] == "help" or tokens[0] == "?":
        print('prefix Expression Evaluator takes in a mathematical expression expressed in prefix notation and evaluates it.')
        print('Example: \"* + 1 2 4 \" will evaluate to \"12\"')
    # Handle quit option
    elif tokens[0] == "quit" or tokens[0] == "q":
        break
    # Handle prefix expression entered
    else:
        value=myStack.evalute(expression)
        print('the result of prefix expression',expression,'is',value)