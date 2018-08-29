def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    if target not in nums:
        return [-1, -1]
    else:
        index = nums.index(target)
        count = nums.count(target)
        return [index, index + count - 1]

if __name__ == '__main__':

    print(searchRange(nums=[5,7,7,8,3,4,3,8,10],target=8))