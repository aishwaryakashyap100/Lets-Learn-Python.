a = 4
b = "4"

print(a is b) # exact location of object in memory
print(a==b) # value
print('  ')

c = [1,2,43]
d = [1,2,43]
print(c is d)
print(c==d)
print(' ')

e = None
f = None
print(e is f)
print(e is None)
print(e == f)