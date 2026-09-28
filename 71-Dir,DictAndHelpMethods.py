# dir() method -

x = [1,2,3]
print(dir(x))
print(x.__add__)

# __dict__ attribute - 

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p = Person('Jhon',30)
print(p.__dict__)

# help() method -

print(help(Person))