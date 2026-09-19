class Employee:
    company = 'Apple'
    def show(self):
        print(f'The name is {self.name} and company is {self.company}')

    @classmethod # If we want class as first argument then we can use this
    def changeCompany(cls,newCompany):
        cls.company = newCompany

e1 = Employee()
e1.name = 'Aish'
e1.show()
e1.changeCompany('Tesla')
e1.show()
print(Employee.company)