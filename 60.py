import itertools

def getPermutation(n, k):
    if n ==1:
        return '1'
    else:
        list = []
        num = 0
        for i in range(1,n+1):
            num = num + i*(10**(n-i))
        str_num = str(num)

        for i in itertools.permutations(str_num, n):
             a = ''.join(i)
             list.append(a)

        print(list[k-1])

if __name__ == '__main__':
    getPermutation(9,4)