class Base1:
    def display(self):
        print("Base1 display method")

class Base2:
    def display(self):
        print("Base2 display method")

class DerivedClass(Base2, Base1):
    pass

obj = DerivedClass()
obj.display()



