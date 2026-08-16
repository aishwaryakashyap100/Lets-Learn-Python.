# Dictionaries are ordered collection of data items

dic = {'Aishwarya':'Human being','Spoon':'Object'}
print(dic['Aishwarya']) # we can access values in the dictionary using keys
print(dic.get('Spoon')) # we can access values in the dictionary by get method also the only difference between both is that if the key is not present get method does not throw any error and returns null
# by these two methods we can access single values
print(dic)


employees = {3:'Manvi',4:'Ashya',78:'Sonyea'}
print(employees[4])
print(employees.keys()) # Accessing keys
print(employees.values()) # Accessing values
# by these two methods we can access multiple items

print(employees.items()) # Accessing key value pairs
for key,value in employees.items():
    print(f'The value corresponding to the key {key} is {value}')

for key in employees.keys():
    print(f'The value corresponding to the key {key} is {employees[key]}')