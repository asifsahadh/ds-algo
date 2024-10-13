# Given a matrix, your task is to rotate the matrix 90 degrees clockwise.

def mat90(matrix):
    
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    for row in matrix:
        row.reverse()
    
    return matrix