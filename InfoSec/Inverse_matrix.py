def determinant_2x2(matrix):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def determinant_3x3(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * determinant_2x2([[e, f], [h, i]]) - b * determinant_2x2([[d, f], [g, i]]) + c * determinant_2x2([[d, e], [g, h]])

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def matrix_minor(matrix, row, col):
    return [row[:col] + row[col + 1:] for row in (matrix[:row] + matrix[row + 1:])]

def matrix_of_minors(matrix):
    return [[determinant_2x2(matrix_minor(matrix, i, j)) for j in range(3)] for i in range(3)]

def matrix_of_cofactors(matrix):
    return [[(-1) ** (i + j) * matrix[i][j] for j in range(3)] for i in range(3)]

def inverse_matrix(matrix):
    det = determinant_3x3(matrix)
    if det == 0:
        raise ValueError("Matrix is not invertible.")
    
    minors = matrix_of_minors(matrix)
    cofactors = matrix_of_cofactors(minors)
    adjugate = transpose(cofactors)
    
    return [[adjugate[i][j] / det for j in range(3)] for i in range(3)]

# Example usage:
A = [[7, -3, -3], [-1, 1, 0], [-1, 0, 1]]
A_inv = inverse_matrix(A)
print(A_inv)