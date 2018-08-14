def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    list =[]
    def clc(star_x,star_y,case,row,col):
        '''
        # starx ,stary, case =[1,2,3,4], row, col
        #
        :return: list
        '''

        if row == 0 or col == 0:
            return list
        if case == 0:
            end_y = star_y+col
            for i in range(star_y, end_y):
                list.append(matrix[star_x][i])
            row -= 1; star_x += 1; star_y = end_y - 1
            case = (case+1)%4
            clc(star_x, star_y, case, row, col)
        elif case==1:
            end_x = star_x + row
            for i in range(star_x, end_x):
                list.append(matrix[i][star_y])
            col -= 1; star_x = end_x -1; star_y -= 1
            case = 2
            clc(star_x, star_y, case, row, col)
        elif case == 2:
            end_y = star_y - col
            for i in range(star_y, end_y, -1):
                list.append(matrix[star_x][i])
            row -=1;star_x -=1; star_y = end_y +1
            case = 3
            clc(star_x, star_y, case, row, col)
        elif case==3:
            end_x = star_x - row
            for i in range(star_x,end_x,-1):
                list.append(matrix[i][star_y])
            col -=1;star_x = end_x+1 ;star_y +=1
            case = 0
            clc(star_x, star_y, case, row, col)
        return list
    row = len(matrix)
    if row ==0:
        return []
    col = len(matrix[0])

    list = clc(0, 0, 0, row, col)
    return list

if __name__ == '__main__':
    matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9,10,11,12]]
    list = spiralOrder(matrix)
    print(list)