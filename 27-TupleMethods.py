# Manipulating tuples -

countries = ('Spain','Italy','India','England','Germany')
temp = list(countries)
temp.append('Russia')     # add item
temp.pop(3)             # remove item
temp[2] = 'Finland'      # change item
countries = tuple(temp)
print(countries)

countries2 = ('Pakistan','Afghanistan','Bangladesh','ShriLanka')
countries3 = ('Vietnam','India','China')
southEastAsia = countries2+countries3
print(southEastAsia) # concatenation

tup = (0,3,4,5,2,4,56,6,4)
res = tup.count(4)
print(res) # returns how many times the element has came into the list

res2 = tup.index(4)
print(res2) # returns the first ocurrance of the given element from the tuple. If element not present in the list then is raises an error

print(len(tup)) # finds the length of the tuple