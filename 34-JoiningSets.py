s1 = {1,2,4,5}
s2 = {3,6,7,2}
print(s1.union(s2)) # union method returns a new set
s1.update(s2) # Update method adds item into the existing set from another set
print(s1,s2)

cities = {'Tokyo','Madrid','Berlin','Delhi'}
cities2 = {'Tokyo','Seoul','Kabul','Madrid'}
cities3 = cities.intersection(cities2)
print(cities3) # Intersection method returns a new set

cities.intersection_update(cities2)
print(cities) # Intersection_update method update into the existing set from another set

cities4 = {'Tokyo','Madrid','Berlin','Delhi'}
cities5 = {'Tokyo','Seoul','Kabul','Madrid'}
cities6 = cities4.symmetric_difference(cities5)
print(cities6) # Symmetric method returns a new set whereas difference_update method updates into the existing set from another set
