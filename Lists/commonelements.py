a = [1,2,3,4,5,6,7,8,9]
b = [5,6,7,8,11,12,13,15]
common = []
for i in a:
    for j in b:
        if(i==j):
            common.append(j)
print(common)