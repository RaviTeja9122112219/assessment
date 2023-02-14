class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display_employee(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)

employee = Employee("Raviteja", 30, 5000)
employee.display_employee()
