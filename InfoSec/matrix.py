# //Multiply 3x3 Matrix with 3x3 Matrix
def multiply(mat1,mat2,mat3):
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                mat3[i][j] += mat1[i][k] * mat2[k][j]
    return mat3

cols =3
rows =3

mat3 = [[0,0,0],[0,0,0],[0,0,0]]
print("Enter the values for the matrix")
mat1 = [[int(input()) for i in range(cols)] for j in range(rows)]
print("Enter the values for the matrix")
mat2 = [[int(input()) for i in range(cols)] for j in range(rows)]

multiply(mat1,mat2,mat3)

print("The resultant matrix is")
for i in range(rows):
    for j in range(cols):
        print(mat3[i][j],end = " ")
    print()