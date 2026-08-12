def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__) # '''Takes in a number n, returns the square of n''' is a docstring which will not appear in output until we print it and it is completely different from comments

def square(n):
    print(n) # if we put anything after the function and then try to put the docstring it will not called as docstring
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__) 

# docstring will be valid only if it is put after the function body

import this # Prints The Zen of python