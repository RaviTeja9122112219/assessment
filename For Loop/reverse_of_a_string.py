a = str(input("enter a string"))
b = []
for i in a:
    b.append(i)
print(''.join(b[::-1]))