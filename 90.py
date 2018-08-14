class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        com_son =[[]]
        if nums!=[]:
            nums.sort()
            for i in range(len(nums)):
                for j in range(len(com_son)):
                    temp = com_son[j] + [nums[i]]
                    if temp in com_son:
                        pass
                    else:
                        com_son.append(com_son[j]+[nums[i]])
        return com_son

if __name__ == '__main__':
    c = Solution()
    nums = [4,1,4,4,4]
    print(c.subsets(nums))