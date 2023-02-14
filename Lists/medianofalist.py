a = [6,4,5,3,2,3,45,6,7,5,43,7,85,6,7,12]
a.sort()
print(a)
print(len(a))
if(len(a)%2==0):
    print((((a[len(a)//2]+a[(len(a)+1)//2])))/2)
    
else:
    print(a[len(a)//2])
    

