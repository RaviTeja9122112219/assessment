class Base:
    def __init__(self, name):
        self.name = name
    def display(self):
        print("Name:", self.name)

class DerivedClass(Base):
    def __init__(self, name, rollno):
        Base.__init__(self, name)
        self.rollno = rollno
    def display(self):
        Base.display(self)
        print("Roll no:", self.rollno)

obj = DerivedClass("Raviteja", "512338107205")
obj.display()



