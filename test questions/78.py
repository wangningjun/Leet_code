class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        com_son =[[]]
        if nums!=[]:
            for i in range(len(nums)):

                for j in range(len(com_son)):

                    com_son.append(com_son[j]+[nums[i]])

        return com_son

if __name__ == '__main__':
    c = Solution()
    nums = [1,2,3]
    print(c.subsets(nums))
