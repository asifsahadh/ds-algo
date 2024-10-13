# Given an integer numRows, return the first numRows of Pascal's triangle.

def generate(numRows):
    if numRows == 0:
        return []
    if numRows == 1:
        return [[1]]
        
    prevRows = generate(numRows - 1)
    newRow = [1] * numRows

    for i in range(1, numRows - 1):
        newRow[i] = prevRows[-1][i - 1] + prevRows[-1][i]

    prevRows.append(newRow)
    return prevRows