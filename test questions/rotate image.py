import time

star = time.time()
def rotate(matrix):

    m = len(matrix)
    n = len(matrix[0])
    matrix = zip(*matrix)
    for i in range(m):
        matrix[i] = list(matrix[i])

    for i in range(m):
        for j in range(int(n / 2)):
            matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
    end = time.time()
    return matrix,end-star

if __name__ == '__main__':

    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print rotate(matrix)

