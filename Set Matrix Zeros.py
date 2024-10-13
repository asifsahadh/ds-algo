# Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then return the matrix.

def zero_row(matrix, num_cols, i):
    for j in range(num_cols):
        if matrix[i][j] != 0:
            matrix[i][j] = -1

def zero_col(matrix, num_rows, j):
    for i in range(num_rows):
        if matrix[i][j] != 0:
            matrix[i][j] = -1

def zero_matrix(matrix, num_rows, num_cols):
    for i in range(num_rows):
        for j in range(num_cols):
            if matrix[i][j] == 0:
                zero_row(matrix, num_cols, i)
                zero_col(matrix, num_rows, j)

    for i in range(num_rows):
        for j in range(num_cols):
            if matrix[i][j] == -1:
                matrix[i][j] = 0

    return matrix