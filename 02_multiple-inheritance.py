class employee:
    company='visa'
    ecode=203

class freelancer:
    company='fiver'
    level=0
    def getlevel(self):
        self.level=self.level+1
        print(f'Level is {self.level}')

class programmer(employee,freelancer):
    name='Rohit'
    def programmerName(self):
        print(f'The programmer Name of {self.company} company is {self.name}')
p=programmer() 
p.programmerName()
print(p.company)
print(p.level)
p.getlevel()
