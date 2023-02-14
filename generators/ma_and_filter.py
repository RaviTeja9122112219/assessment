
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#map
square = list(map(lambda x: x**2, num))
print("Square numbers:", square)

#filter
even_numbers = list(filter(lambda x: x % 2 == 0, num))
print("Even numbers:", even_numbers)

