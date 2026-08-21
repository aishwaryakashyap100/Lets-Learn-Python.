a = int(input('Enter any value between 5 and 9:'))

if(a<5 or a>9):
    raise ValueError('Value should be between 5 and 9')

salary = int(input('Enter salary amount:'))
if not 2000<salary<5000:
    raise ValueError('Not a valid salary')

a = input("Enter any value between 1 and 5:")

if a == "quit":
    print("Exiting the program")
else:
    try:
        a = int(a)
        if a < 1 or a >5:
            raise ValueError("Value must be between 1 and 5")

    except ValueError:
        print("Invalid input, please enter a valid number between 1 and 5 or type 'quit' to exit")
