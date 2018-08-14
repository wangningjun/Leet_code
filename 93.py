class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def clc(s,k,oip,reip):  # 递归函数，结束条件为四个点加完
            if k == 4:
                if s == '':
                    reip.append(oip[1:])
                return

            for i in range(1,4):
                if i <=len(s):   # 防止i超额
                    if int(s[:i])>255:
                        break
                    else:
                        clc(s[i:],k+1,oip+'.'+s[:i],reip)
                        if s[0]=='0':
                            break

            return reip
        reip =[]
        result= clc(s,0,'',reip)
        return result
if __name__ == '__main__':
    s = Solution()
    str = "010010"
    print(s.restoreIpAddresses(str))