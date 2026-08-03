# Loops - sometimes a programmer wants to execute a group of statements a certain number of times. This can be done through looping

# For loop - it can iterate over a sequence of iterable objects in pyhton. Iterating over a sequence is nothing but iterating over strings, lists, tuple, sets and dictionaries
name = 'Aishwarya'
for i in name:
    print(i)
    if (i=='w'):
        print('This is something special') # For strings

colors = ['red','green','yellow','blue']
for color in colors:
    print(color)
    for i in color:
        print(i) # for list

for i in range(5):
    print(i+1)

for i in range(1,101):
    print(i)

for i in range(1,12,2): # the third parameter skips the next number according to the given number in the third parameter
    print(i)
