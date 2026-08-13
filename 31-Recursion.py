# Recursion is the process of defining something in terms of itself

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

print (factorial(7))

# python recursive functions -

def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)

num = 7
print('Number:',num)
print('Factorial:',factorial(num))