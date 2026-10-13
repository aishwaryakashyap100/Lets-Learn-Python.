a = True
print(a:= False)

# While loop example -
numbers = [1,2,3,4,5]

while (n:= len (numbers))>0:
    print(numbers.pop())

# Another Example -

happy = False
print(happy)

print(happy :=True)

# Another Example -
foods = list()
while True:
    food = input('What food do you like?: ')
    if food == 'quit':
        break
    foods.append(food)

# Above example using walrus operator - 

foods = list()
while (food := input('What food do you like?: ')) != 'quit':
    foods.append(food)