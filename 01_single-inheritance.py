class employee:
    company='Google'
    
    def ShowDetails(self):
        print('This is a empolyee')
        print(f'This is a employee in company {self.company}')
    
class Programmer(employee):
    language='Python'

    def GetLanguage(self):
        print('This is an Python Programmer')
        print(f'This programmer only know {self.language} language')

e=employee()
# e.ShowDetails()
p=Programmer()
p.GetLanguage() 
p.ShowDetails()
print(p.company)
