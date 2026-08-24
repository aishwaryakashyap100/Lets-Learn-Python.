# Enumerate function allows you to loop over a sequence(such as a list,tuple, or string) and get the index and value of each element in the sequence at the same time

marks = [12,56,32,98,12,45,1,4]

index = 0
for mark in marks:
    print(mark)
    if index==3:
        print("Awesome!")
    index+=1

# Enumerate function example-

for index,mark in enumerate (marks):
    print(mark)
    if index==3:
        print("Awesome!")

fruits = ['apple','banana','mango']
for index, fruit in enumerate(fruits):
    print(index,fruit)

# Changing the start index-

for index, fruit in enumerate(fruits, start=1):
    print(index,fruit)