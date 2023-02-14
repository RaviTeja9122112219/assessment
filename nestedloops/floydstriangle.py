a = int(input("enter number of rows"))
b = 1
for i in range(0,a+1):
    for j in range(0,i):
        print(b,end = " ")
        b = b+1
    print()
