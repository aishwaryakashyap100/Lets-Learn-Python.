# Tuples are ordered collection of data but they are unchangeable(everything is same as list but tuples are immutable)

tup1 = (1,6,4,3,6,8)
tup2 = ('Red','Blue','Green','Yellow')
print(tup1)
print(tup2)
print(type(tup1))
print(tup1[4])

details = ('Aishwarya',18)
print(details)

if 3 in tup1:
    print("Present")

print(tup1[2:5]) # It will not change the existing tuple but makes a new tuple

