def fib(n):
    a = 0
    b = 1
    while n > 0:
        print(a)
        a, b = b, a + b
        n = n - 1


fib(20)
