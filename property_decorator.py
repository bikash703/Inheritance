class employee:
    salary = 6000
    salaryBonus = 1000

    @property        #This is called Getter Method or Property Decorator
    def TotalSalary(self):
        return self.salary + self.salaryBonus

e=employee()
print(e.TotalSalary)