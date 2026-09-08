class Person:
    name = 'Harry'
    occupation = 'Software Developer'
    networth = 10,000
    def info(self):
        print(f'{self.name} is a {self.occupation}')

a = Person()
b = Person()
a.name = 'shubham'

b.name = 'Nitika'
b.occupation = 'HR'
a.occupation = "Accountant"
# print(a.name,a.occupation)
a.info()
b.info()