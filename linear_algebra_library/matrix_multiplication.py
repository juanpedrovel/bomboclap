
def transpose(matrix):
    matrix_transpose = []
    for j in range(len(matrix[0])):
        matrix_transpose.append([])
        for i in range(len(matrix)):
            matrix_transpose[j].append([])
            matrix_transpose[j][i] = matrix[i][j]
    
    return matrix_transpose


def dot_product(vector_one, vector_two):
    result = 0
    for i in range(len(vector_one)):
        result += vector_one[i]*vector_two[i]
    return result


def matrix_multiplication(matrixA, matrixB):
    product = []
    matrixB_transposed = transpose(matrixB)
    
    for i in range(len(matrixA)):
        product.append([])
        for j in range(len(matrixB_transposed)):
            product[i].append(dot_product(matrixA[i], matrixB_transposed[j]))

    return product


def identity_matrix(n):
    identity = []
    for i in range(n):
        identity.append([])
        for j in range(n):
            if i == j:
                identity[i].append(1)
            else:
                identity[i].append(0)
    
    return identity