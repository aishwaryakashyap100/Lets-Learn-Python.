# While loop - it execute statements while the condition is true.As soon as the condition becomes false, the interpreter comes out of the while loop
i = 0
while i<=3:
    print(i)
    i = i+1 

i = int(input('Enter the number: '))
while(i<=35):
    i = int(input('Enter the number: '))
    print(i)

print("Done with the loop")

count = 5
while (count>0):
    print(count)
    count = count - 1 # Decrementing loop
    # If we will take +1 inestead of -1 it will become ifinite loop
else:
    print('I am inside else') # we can also use the else statement

# Do while loop - execute one time whether the condition is true or not
while True:
    number = int(input("Enter a positive number: "))
    print(number)
    if not number > 0:
        break