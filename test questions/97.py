class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        s1_len = len(s1)
        s2_len = len(s2)
        s3_len = len(s3)


        if s1_len+s2_len != s3_len:
            return False
        matrix = [[0] * (s2_len + 1) for _ in range(s1_len + 1)]
        matrix[0][0] = 1
        for i in range(s1_len+1):
            for j in range(s2_len+1):
                if i!=s1_len and s1[i] == s3[i+j]:
                    if matrix[i+1][j] ==1:
                        continue
                    else:
                        matrix[i+1][j] = matrix[i][j]
                if j!=s2_len and s2[j] == s3[j+i]:
                    if matrix[i][j+1] ==1:
                        continue
                    else:
                        matrix[i][j+1] = matrix[i][j]

        print(matrix)
        if matrix[s1_len][s2_len] == 1:
            return True
        else:
            return False


if __name__ == '__main__':
    s1 = "aabc"
    s2 = "abad"
    s3 = "aabcabad"
    S = Solution()
    print(S.isInterleave(s1,s2,s3))
