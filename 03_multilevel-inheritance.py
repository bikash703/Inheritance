class person:
    country='india'
    
    def takebreath(self):
        print('I am Breathing..')

class employee(person):
    company='google'
    salary=5000
    
    def getsalary(self):
        print(f"Salary is {self.salary}")
    
    def takebreath(self):
        print('I am an employee so i am slightly Breathing')

class programmer(employee):
    company='Fiverr'
    
    def getsalary(self):
        print('No salary for programmer')

pr=programmer()
pr.getsalary()
pr.takebreath()
p=person()
p.takebreath()
e=employee()
print(e.company)
e.getsalary()
