x = 10 # Global variables

def my_function():
    global x # this is a global keyword
    x = 4 # this will change the value of the global variable x
    y = 5
    print(y)

my_function()
print(x)
# print(y) this will cause an error because y is a local variable and is not accessible outside of the function