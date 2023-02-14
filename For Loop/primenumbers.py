a= int(input("Please Enter the Range Value:"))

for i in range(1,a+1):
    count = 0
    for j in range(2,i):
        if(i % j == 0):
            count = count + 1
            break
            

    if (count == 0 and i!= 1):
        print(i)