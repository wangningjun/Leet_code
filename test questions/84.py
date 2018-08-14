class Solution:
    def __init__(self,matrix):
        self.matrix = matrix
    def maximalRectangle(self):
        row = len(self.matrix)
        col = len(self.matrix[0])
        if row==0 or col==0 or self.matrix==[[]]:
            return 0
        max_area = 0
        height = [0]*col
        for i in range(row):
            for j in range(col):
                if self.matrix[i][j] == "1":
                    height[j]+=1
                else:
                    height[j] = 0
            heights = height
            area = self.largestRectangleArea(heights)
            max_area = max(area,max_area)
        return max_area
    def largestRectangleArea(self,heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        stack = [0]
        heights.append(0)
        max_area = 0
        for i in range(len(heights)):
            if heights[i] >= stack[-1]:
                stack.append(heights[i])
            else:
                k = len(stack) - 1
                count = 0
                while heights[i] < stack[k] and k >= 0:
                    count += 1
                    area = count * stack[k]
                    if max_area < area:
                        max_area = area
                    k -= 1
                stack = stack[:-count] + [heights[i],] * (count + 1)
        return max_area

if __name__ == '__main__':
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    c = Solution(matrix)
    print(c.maximalRectangle())
