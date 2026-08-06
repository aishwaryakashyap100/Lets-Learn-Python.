'''Function arguments are of four types

1. Default Arguments - We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument
2. Keyword Arguments - we can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name
3. Variable Length Arguments - It is necessary to pass the arguments
4. Requires Arguments - Sometimes we may need to pass more arguments than those defined in the actual function for this we use this argument'''

def average(a=9,b=8):
    print('The average is ', (a+b)/2)

average(6,4) # This is example of default arguments

def name(fname,mname = 'Aishwarya', lname = 'Kashyao'):
    print("Hello,", fname, mname, lname)

name("Siddhi", 'Aish') # This is example of keyword arguments

def average(a,b,c = 1):
    print('The average is ', (a+b+c)/2)

average(5,8)
def name(fname,mname,lname):
    print('Hello',fname,mname,lname)

name('Peter','Ego','Quill') # Both are example of required arguments

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print ('Average is:', sum/len(numbers))

average(5,6)
def name(*name):
    print("Hello",name[0], name[1], name[2])

name('James','Buchanan','Barnes') # variable length argument can be of two types this is the example of arbitrary arguments

def name(**name):
    print('Hello,',name['fname'], name['mname'], name['lname'])

name(mname = "Rai", lname = 'Bacchan', fname = 'Aishwarya') # This is the example of keyword arbitrary arguments

# The return statement is used to return the value of the expression back to the calling function
def name(fname,mname,lname):
    return 'Hello,' + fname + " " + mname + " " + lname

print(name('James','Buchanan', 'Barnes')) # This is the example of return statement