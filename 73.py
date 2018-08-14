def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    row = len(matrix)
    col = len(matrix[0])
    a=[1]*row
    b=[1]*col
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] ==0:
                a[i] = 0
                b[j] = 0

    for i in range(row):
        if a[i] == 0:
            matrix[i] = [0]*col
    for j in range(col):
        if b[j] == 0:
            for i in range(row):
                matrix[i][j] = 0
    return matrix

if __name__ == '__main__':
    matrix = [[1, 6, 3], [2, 3, 0], [3, 2, 4]]
    M = setZeroes(matrix)
    print(M)

