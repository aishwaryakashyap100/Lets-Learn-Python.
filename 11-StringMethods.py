names = "Aishwarya,Siddhi"
print(len(names)) # Finds the length of the string

#strings as an array -
print(names[0:5]) #It prints the first five characters
# This is also known as slicing
print(names[0:-5]) # It minus the ending characters and print the staring ones whcih is left
print(names[-3:-1])
a = 'Aishwarya'
print(a[-5:-3])

print(a.upper()) # It changes the string in capital letter
print(a.lower()) # It changes the string in small letter

b = '!!!Aish!!!'
print(b.strip("!")) # It removes the trailing characters
print(a.replace('Aishwarya','Aishu')) # It replaces all the occurences of a string with another string

c = '!!!Aish!!! !!!Aish!!!'
print(c.split()) # This method splits at the specified instance and returns the separated strings as list items

weather = 'today\'s Weather is good!'
print(weather.capitalize()) # It capitalizes the first letter and the rest in small letter

str1 = "Welcome to the Console!!!"
print(len(str1))
print(str1.center(50)) # It aligns the string to the center as per the parameters given by the user
print(len(str1.center(50))) # It adds 25 spaces more to make it 50

print(c.count('Aish')) # It counts the number of times the given value has occured within the given string

print(str1.endswith('!!!')) # It checks if the string ends with the given value. If yes then it returns true, else false
print(str1.endswith('to',4,10))
print(str1.startswith('Welcome')) # It checks if the string starts with the given value. If yes then it returns true, else false

print(str1.find('to')) # It searches for the first occurance of the given value and returns the index where it is present. If given value is absent from the string then return -1
print(str1.index('to')) # It is similar to find but it raises an error if the given value is not present

print(str1.isalnum()) # It returns true if the entire string only cosists of A-Z,a-z,0-9
print(str1.isalpha()) # It returns true if the entire string only consists of A-Z,a-z

print(str1.isupper()) # It returns true if the entire string is in upper case
print(str1.islower()) # It returns true only if the entire string is in lower case

d = "Hello! How are you?\n"
e = "Hello! How are you?"
print(d.isprintable()) # It returns true if all the values within the given string is printable
print(e.isprintable())

print(e.isspace()) # It returns true if string contains only of white spaces

print(str1.istitle()) # Returns true only if the first letter of each word of the string is capitalized

print(str1.swapcase()) # changes the character casing of the string. Upper case are converted into lower case and lower case are converted into upper case
print(str1.title()) # Capitalizes each letter of the word within the string