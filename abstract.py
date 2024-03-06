from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self,firstname, lastname):
        self.firstname= firstname
        self.lastname= lastname
    
    @property    
    def fullname(self):
        return f"{self.firstname} {self.lastname}"
    
    @abstractmethod    
    def salary(self):
        pass
    
class Fulltimeemployee(Employee):
    def __init__(self, firstname, lastname, salary):
        super().__init__(firstname, lastname)
        self._salary = salary

    @property
    def salary(self):
        return self._salary



        
class halftimeemployee(Employee):
    def __init__(self,firstname, lastname, rate,hour):
        super().__init__(firstname, lastname)
        self.rate=rate
        self.hour= hour

    @property    
    def salary(self):
        return self.rate * self.rate
        
        
class Payroll:
    def __init__(self):
        self.employee_list=[]
        
    def add(self,Employee):
        self.employee_list.append(Employee)
        
    def print(self):
        for e in self.employee_list:
            print(e.fullname, e.salary)
            
            
payroll = Payroll()

payroll.add(Fulltimeemployee('John', 'Doe', 6000))
payroll.add(Fulltimeemployee('Jane', 'Doe', 6500))
payroll.add(halftimeemployee('Jenifer', 'Smith', 200, 50))

payroll.print()
    
