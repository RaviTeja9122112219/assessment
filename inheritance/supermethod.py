class Ravi:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_Ravi(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Employee(Ravi):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
    
    def display_employee(self):
        super().display_Ravi()
        print("Salary:", self.salary)

# Create an Employee object and call its display_employee method
employee = Employee("Raviteja", 30, 50000)
employee.display_employee()
