def armstrong(n):
    maxi = n
    sum = 0
    num_of_digits = len(str(n))
    while n > 0:
        digit = n % 10
        sum = sum + digit ** num_of_digits
        n = n // 10
    return sum == maxi


result = armstrong(153)
print(result)
