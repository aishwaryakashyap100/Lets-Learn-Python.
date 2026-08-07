# Lists are ordered collection of data items
list1 = [5,8,9,6,7,3]
list2 = ['Apple,','Mango','Banana']
print(list1)
print(list2)
print(list1[0])
print(list2[2])
print(list1[-1])
print(list1[len(list1)-2])

if 'Mango' in list2:
    print("yes")
else:
    print('No')

if 'ang' in "Mango":
    print("yes")
else:
    print('no')

print(list1[1:-1])
print(list1[1:4:2]) # first it does slicing and then jumps to the second value according to the given slicing

lst = [i*i for i in range(10)]
lst2 = [i*i for i in range(10)if i%2==0]
print(lst)
print(lst2)