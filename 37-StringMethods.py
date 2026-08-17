ep1 = {122:45,123:89,567:69}
ep2 = {222:67,566:90}

ep1.update(ep2) # update() method updates the value of the key provided to it if the item already exists in the dictionary,else it creates a new key-value pair
print(ep1)

ep1.clear() # clear method removes all the items from the list
print(ep1)

ep3 = {122:45,123:89,567:69}
ep3.pop(122) # pop method removes the key-value pair whose key is passed as a parameter
print(ep3)

ep3.popitem() # popitem method removes the last key-value pair from the dictionary
print(ep3)

del ep2[222] # Del keyword is used to remove a dictionary item
print(ep2)
