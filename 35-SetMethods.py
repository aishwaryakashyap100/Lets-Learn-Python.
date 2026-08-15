cities = {'Tokyo','Madrid','Berlin','Delhi'}
cities2 = {'Tokyo','Seoul','Kabul','Madrid'}
print(cities.isdisjoint(cities2)) # isdisjoint() method checks if items of given set are present in another set
cities3 = {'Seoul','Kabul'}
print(cities.issuperset(cities3))
cities4 = {'Tokyo','Madrid','Delhi'}
print(cities.issuperset(cities4)) # issuperset checks if all items of a particular set are present in the original set
print(cities.issubset(cities4)) # issubset checks if all the items of the original set are present in the particular set

cities.add('Helsinki')
print(cities) # if you want to add a single item to the set use the add() method

cities5 = {'Helsinki','Seoul'}
cities2.update(cities5)
print(cities2) # if you want to add more than one item, simply create another set or any other iterable object

cities.remove('Delhi')
print(cities) # Remove raises an error if the item is not present whereas discard does not raise any error
cities.discard('Japan')

item = cities.pop()
print(cities)
print(item) # pop method removes the last item of the set but the catch is that we dont know which item gets popped as sets are unordered

del cities # It is not a method, rather it is a keyword which deletes the set entirely

cities2.clear()
print(cities2) # This method clears all items in the set and prints an empty set

# Check if item exists

info = {'Carla',19,False,5.9}
if 'Carla' in info:
    print('Carla is present')
else:
    print('Carla is absent')