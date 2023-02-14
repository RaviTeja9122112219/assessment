class Employee:
    def __init__(self, name, age, salary, department, contact_info):
        self.name = name
        self.age = age
        self.salary = salary
        self.department = department
        self.contact_info = contact_info

class ContactInformation:
    def __init__(self, email, phone):
        self.email = email
        self.phone = phone

class EmployeeSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)

    def update_employee(self, employee, updated_info):
        employee.contact_info = updated_info

    def display_employees(self):
        for employee in self.employees:
            print("Name:", employee.name)
            print("Age:", employee.age)
            print("Salary:", employee.salary)
            print("Department:", employee.department)
            print("Contact Information:", employee.contact_info.email, employee.contact_info.phone)
            print("\n")

# Example usage of the Employee System
employee_system = EmployeeSystem()

contact_info = ContactInformation("Ravi@gmail.com", "7032043837")
employee = Employee("Raviteja", 30, 100000, "Engineering", contact_info)

employee_system.add_employee(employee)
employee_system.display_employees()

