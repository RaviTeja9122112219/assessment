class Car:
    def __init__(self, model, year, make):
        self.model = model
        self.year = year
        self.make = make

    def display_car(self):
        print("Model:", self.model)
        print("Year:", self.year)
        print("Make:", self.make)

car = Car("shiftdezire", 2022, "suzuki")
car.display_car()
