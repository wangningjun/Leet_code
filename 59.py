def generateMatrix(n,mat):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """

    def clc(star_x,star_y,case,row,col,count):
        '''
        # starx ,stary, case =[1,2,3,4], row, col
        #
        :return: list
        '''

        if row == 0 or col == 0:
            return mat
        if case == 0:
            end_y = star_y+col
            for i in range(star_y, end_y):
                mat[star_x][i] = count
                count +=1
            row -= 1; star_x += 1; star_y = end_y - 1
            case = (case+1)%4
            clc(star_x, star_y, case, row, col, count)
        elif case==1:
            end_x = star_x + row
            for i in range(star_x, end_x):
                mat[i][star_y] = count
                count += 1
            col -= 1; star_x = end_x -1; star_y -= 1
            case = 2
            clc(star_x, star_y, case, row, col,count)
        elif case == 2:
            end_y = star_y - col
            for i in range(star_y, end_y, -1):
                mat[star_x][i] = count
                count += 1
            row -=1;star_x -=1; star_y = end_y +1
            case = 3
            clc(star_x, star_y, case, row, col,count)
        elif case==3:
            end_x = star_x - row
            for i in range(star_x,end_x,-1):
                mat[i][star_y] = count
                count += 1
            col -=1;star_x = end_x+1 ;star_y +=1
            case = 0
            clc(star_x, star_y, case, row, col,count)
        return mat
    row = n
    if row ==0:
        return []
    col = n
    count = 1
    mat = clc(0, 0, 0, row, col,count)
    return mat

def matrix(n,m):
    a = []
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(0)
        a.append(temp)
    return a

if __name__ == '__main__':
    n = 4
    mat = matrix(n,n)
    # matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9,10,11,12]]
    list = generateMatrix(n,mat)
    print(list)