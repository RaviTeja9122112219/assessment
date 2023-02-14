def fib(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

for num in fib(20):
    print(num)
