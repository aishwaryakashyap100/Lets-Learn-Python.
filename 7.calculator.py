# Simple calculator program

print("Enter the first number :")
a = int(input())
print("Enter the second number :")
b = int(input())

print("Enter the operation you want to perform : + _ * /")
operation = input()

if operation =='+':
    print("The addition of two numbers is :",a+b)
if operation =='_':
    print("The subtraction of two numbers is :",a-b)
if operation =='*':
    print("The multiplication of two numbers is :",a*b)
if operation =='/':
    print("The division of two numbers is :",a/b)