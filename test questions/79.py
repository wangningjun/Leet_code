class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        col = len(board[0])
        row = len(board)
        index = [[False]*col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                if self.clc_exist(board, word, 0,i, j,index):
                    return True
        return False

    def clc_exist(self,board, word,count,i,j,index ):
        if count==len(word):
            return True

        # i>=len(board)一定需要等号
        if i<0 or j <0 or i>=len(board) or j>=len(board[0]) or index[i][j] or board[i][j]!=word[count]:
            return False
        index[i][j] = True
        result = self.clc_exist(board,word,count+1,i-1,j, index) or \
                 self.clc_exist(board,word,count+1,i,j-1, index) or \
                 self.clc_exist(board,word,count+1,i+1,j, index) or \
                 self.clc_exist(board,word,count+1,i,j+1, index)
        index[i][j] = False

        return result

if __name__ == '__main__':
    search = Solution()
    board = [['a']]
    word = 'ab'
    result = search.exist(board,word)
    print(result)