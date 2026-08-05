# Functions is a block of code that performs a specific task whenever it is called

def calculateGmean(a,b):
    mean = (a*b/(a+b))
    print(mean)

def isGreater(a,b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is greater")

def isLesser(a,b):
    pass # This can be used to write the program later

a = 3
b = 2

calculateGmean(a,b)
isGreater(a,b)

c = 8
d = 9

calculateGmean(c,d)
isGreater(c,d)

