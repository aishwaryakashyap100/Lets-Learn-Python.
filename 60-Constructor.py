class Person:

    def __init__(self,n,o):
     print("Hey I am a person") # This is example of default constructor
     # self.name = name
     self.name = n
     self.occ = o # This is example of self constructor

    def info(self):
        print(f'{self.name} is a {self.occ}')
        # Person()

a = Person("Harry","Developer")
b = Person('Divya',"HR")
a.info()
b.info()
print(a.name)
a.name = 'Divya'
a.occ = 'HR'
a.info()