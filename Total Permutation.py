'''
实现字符串的全排列
'''

s = [1,2,3,4]

def permutation(s,sta,end):

    if sta ==end:
        for i in s:
            print(i,end='')
        print()
    else:
        for i in range(sta,end):
            s[i],s[sta] = s[sta],s[i]
            permutation(s,sta+1,end)
            s[sta], s[i] = s[i], s[sta]

if __name__ == '__main__':
    sta = 0
    end = len(s)
    permutation(s,sta,end)


