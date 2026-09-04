# Map - 
# def cube (x):
#     return x*x*x

# print(cube(2))
l = [1,2,3,4,6,8]

# newl = []
# for item in l:
#     newl.append(cube(item))
# print(newl)

newl = list(map(lambda x:x*x*x,l))
print(newl)

# Filter -
def filter_function(a):
    return a>4

newnewl = list(filter(filter_function,l))
print(newnewl)

# Reduce -
from functools import reduce

numbers = [1,2,3,4,5]

sum = reduce(lambda x,y:x+y,numbers)

print(sum)