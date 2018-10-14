class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_a = 0
        left =0
        right = len(height) -1
        while right > left:
            max_a = max(max_a, (right-left)*min(height[left], height[right]))
            if height[right]>height[left]:
                left+=1
            else:
                right-=1
        return max_a

if __name__ == '__main__':
    S = Solution()
    h = [1,8,6,2,5,4,8,3,7]
    print(S.maxArea(h))
