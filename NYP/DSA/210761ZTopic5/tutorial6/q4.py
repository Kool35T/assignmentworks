def isPalindrome(aStr):
    # Base case
    if len(aStr) <= 1:
        return True
    
    return aStr[0] == aStr[-1] and \
        isPalindrome(aStr[1 : len(aStr) - 1]) # Recursive case
        
# Test code
while True:
    aStr = input('Enter a string (q to quit): ')
    aStr = aStr.lower()
    
    if aStr == 'q':
        break
    
    # Strip all non-alphanumeric characters from aStr
    aStr = ''.join(ch for ch in aStr if ch.isalnum())
    
    # Call isPalindrome() to determine if aStr is a palindrome
    is_a_palindrome = isPalindrome(aStr)
    
    if is_a_palindrome:
        print("'{}' is a palindrome.".format(aStr))
    else:
        print("'{}' is not a palindrome.".format(aStr))