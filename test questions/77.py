def combine(n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """

    def clc(i,n,k,temp):
        if k ==0:
            result.append(temp)
            return
        for j in range(i+1,n+1):
            clc(j,n,k-1,temp+[j])

    result = []
    clc(0,n, k, [])
    return result
if __name__ == '__main__':
    print(combine(4,3))

