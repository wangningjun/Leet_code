class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        begin = 0
        end = 0
        if nums is []:
            return 0
        len_nums = len(nums)
        count = len_nums
        for i in range(1,len_nums):
            if nums[i-1] == nums[i]:
                end = i
            else:
                begin = end =i
            if end - begin >=2:
                count-=1

        return count

if __name__ == '__main__':
    c = Solution()
    num = [1,1,1,2,2,2,2,2,2,3,3,3]
    result = c.removeDuplicates(num)
    print(result)

