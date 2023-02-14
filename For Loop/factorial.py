a = int(input("enter a number "))
result = 1
for i in range(1,a+1):
    if(a==1):
        print(0)
        break
    else:
        result = result*i
print(result)
