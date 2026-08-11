name = "Aishwarya"
country = 'India'
print(f'Hey my name is {name} and I am from {country}')

# String formatting - 
txt = 'For only {price:.2f} dollars!'
print(txt.format(price = 49.09999)) # If you want to take floating value with two decimals this can be used

# same thing can be done using f-strings
price = 49.0999
txt2 = f'For only {price:.2f} dollars!'
print(txt2)

print(f'{2*30}') 
print(type(f'{2*3}'))

print(f'We use f-strings like this: Hey my name is {{name}} and i am from {{country}}') # if you want to show whats written inside curly brakets then this can be done