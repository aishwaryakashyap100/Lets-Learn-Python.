# Public access specifier -
class Student:
    def __init__(self,name,age):
        self.age = age
        self.name = name

obj = Student(21,'Harry')
print(obj.age)
print(obj.name)

# Private access modifier -
class Employee:
    def __init__(self):
        self.__name = 'Aish'

a = Employee()
# print(a.__name) # Cannot be accessed directly
print(a._Employee__name) # Can accessed it indirectly

# Protected access modifier -
class Student:
    def __init__(self):
        self._name = 'Aish'

    def _funName(self): # Protected method
        return 'CodeWithAish'

class Subject(Student): # Inherited class
    pass

obj = Student()
obj1 = Subject()
print(dir(obj)) # Name Mangling

# Calling by object of Student class
print(obj._name)
print(obj._funName())
# Calling by object of Subject class
print(obj1._name)
print(obj1._funName())