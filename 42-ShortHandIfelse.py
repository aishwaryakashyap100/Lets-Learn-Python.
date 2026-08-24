# This is a shorthand syntax for if else statement that can be used when the condition being tested is simple and the code blocks to be executed are short

a = 330
b = 3303
print("A") if a>b else print("=") if a == b else print("B")

if a>b:
    print("A")
if a ==b:
    print("=")
else:
    print("B") # By using shorthand you can write the conitions in one line rather than writing the code in multiple lines