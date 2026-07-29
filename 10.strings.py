# Anything that is written inside quotation marks are called strings
x = "Hello"
print(x)

# Multiple line strings -
a = '''Hello how are you?
I am good! And what about you?
I am also good!'''
print(a)

# Accessing characters of a string
print(x[0])
print(x[1])
print(x[2])
print(x[3])
print(x[4])
# print(x[5]) throws an error

# Looping through strings
print("By using for loop\n")
for character in x:
 print(character)