import os 

print("Hello world from...")
os.system("Python3 --version")
# by this we can know the version of the python

# A match case will compare the value with the given cases untill the required case is matched

x = int(input('Enter the number: '))

match x:
    case 0:
        print('x is zero')
    case 4:
        print('x is four')
    case _: # default case
        print(x)