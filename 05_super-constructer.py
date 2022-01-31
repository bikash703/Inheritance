class Woner:
    Company = 'Infosys'
    City = 'Bhubaneswar'

    def __init__(self):
        print('The  Woner Name is Harry')

    def GetWoner(self):
        print("I want Some Employee's")
    
class Employee(Woner):
    City = 'Cuttack'

    def __init__(self):
        super().__init__() 
        print('The Company Employee Name is Rajesh')

    def GetEmployee(self):
        super().GetWoner()
        print("I want some Programmers")

class Programmer(Employee):
    City = 'Jajpur'

    def GetProgrammer(self):
        super().GetEmployee()
        print('Your Software is ready')


# w=Woner()

# e=Employee()

p=Programmer()
p.GetProgrammer()
