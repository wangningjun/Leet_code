def minDistance(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    len_1 = len(word1)
    len_2 = len(word2)

    dict = [[0]*(len_2+1) for _ in range(len_1+1)]
    if len_1==0 and len_2==0:
        return 0
    if len_1==0 and len_2>0:
        return len_2
    if len_2==0 and len_1>0:
        return len_1
    # if len_1==0 or len_2==0:
    #     return len_1 if len_1!=0 else len_2
    if len_2>0 and len_1>0:
        for i in range(len_1+1):
            dict[i][0] = i
        for j in range(len_2+1):
            dict[0][j] = j
        for i in range(1,len_1+1):
            for j in range(1,len_2+1):
                if word1[i-1] == word2[j-1]:
                    dict[i][j] = dict[i-1][j-1]
                else:
                    dict[i][j] = min(dict[i-1][j],dict[i][j-1],dict[i-1][j-1]) +1
    return dict[len_1][len_2]

if __name__ == '__main__':
    word1 = 'cafe'
    word2 = 'coffee'
    print(minDistance(word1,word2))