#input_from_the_user

row1 = int(input("enter number of rows fro matrix 1"))
column1 = int(input("enter number of columns for matrix 1"))

matrix1 = []

for i in range(row1):
    a = []
    for j in range(column1):
        a.append(int(input()))
    matrix1.append(a)


#print(len(matrix))
#for printing the matrix
# for i in range(row):
#     for j in range(column):
#         print(matrix[i][j], end = " ")
#     print()


#taking input from user for second matrix
row2 = int(input("enter number of rows for second matrix"))
column2 = int(input("enter number of columns for second matrix"))
matrix2 = []
for i in range(row2):
    b = []
    for j in range(column2):
        b.append(int(input()))
    matrix2.append(b)

# print()

# for i in range(row):
#     for j in range(column):
#         print(matrix[i][j], end = " ")
#     print()

# print()
# for i in range(row1):
#     for j in range(column1):
#         print(matrix1[i][j], end = " ")
#     print()

# print()

#******************************adding two matrices***********************************************
                               #add = [[0,0],[0,0]]
result = []
for i in range(row1):
    c = []
    for j in range(column1):
        c.append(0)
    result.append(c)


for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j] = matrix1[i][j] + matrix2[i][j]
        print()

for i in  result:
    print(i)



#transpose of a matrix

transpose = []
for i in range(row1):
    c = []
    for j in range(column1):
        c.append(0)
    transpose.append(c)

for i in range(row1):
    for j in range(column1):
        transpose[j][i]=matrix1[i][j]
print()
print()    
for i in transpose:
    print(i)


print()
print()
print("#########multiplication of two matrices###########")

# multiplication = []
# for i in range(len(matrix)):
#     m = []
#     for j in range(len(matrix1[0])):
#         m[i][j].append(0)
#     multiplication[i][j].append(m)


multiplication = []
for i in range(len(matrix1)):
    m = []
    for j in range(len(matrix2[0])):
        m.append(0)
    multiplication.append(m)

for i in range(len(matrix1)):
    for j in range(len(matrix2[0])):
        for k in range(len(matrix2)):
            multiplication[i][j] += matrix1[i][k] * matrix2[k][j]

for i in multiplication:
    print(i)   
