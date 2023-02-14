def prime_numbers(n):
    def prime(num):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    return False
            else:
                return True
        else:
            return False

    for num in range(2, n+1):
        if prime(num):
            yield num

for i in prime_numbers(100000):
    print(i)
