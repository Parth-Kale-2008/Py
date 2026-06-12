class Employee:
    def __init__(self,salary,name,bond):
        self.salary = salary
        self.name = name
        self.bond = bond
        
    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"the name of the employee is {self.name}. salary is {self.salary}. the bond is for{self.bond} years")
        
        
e1 = Employee(34000,"Tanishq",4)
print(e1.get_salary())

    