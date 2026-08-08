# List Methods -

l = [4,3,5,2,6]
l.append(7)
print(l) # This method adds value at the end of the list

l.sort() 
print(l) # This method sorts the list in ascending order 

l.sort(reverse=True)
print(l) # This method sorts the list in decending order

i = [4,2,7,1,8,5,1]
print(i.index(4)) # gives the index of the first occurrence of the list item

i.reverse()
print(i) # This method reverse the original value of the list

print(i.count(1)) # counts how many times the number has came into the list

m = l.copy()
print(l) # This method returns the copy of the list

i.insert(1,44)
print(i) # This method inserts an item at the given index

m = [50,60,30]
k = i+m # concatenates i and m (join two lists)
print(k)
i.extend(m)
print(i) # This method adds the entire list or any other collection datatype