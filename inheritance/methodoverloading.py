class summ:
    def add(self, a, b=0):
        return a + b

# with two arguments
adding = summ()
result = adding.add(10, 5)
print("Result:", result)

# with one argument
result = adding.add(10)
print("Result:", result)
