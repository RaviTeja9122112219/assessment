a = [1,2,3,2,2,3,4,5,6,5,7,8,8,9,10]
b = []
for i in a:
    if(a.count(i)<=1):
        b.append(i)
print(b)