def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    for i in range(len(nums)):
        if nums[i] !=0:
            continue
        else:
            if i==len(nums)-1:
                return True
            else:
                temp = nums[:i+1][::-1]
                flag = False
                for j,num in enumerate(temp):
                    if num > j:
                        flag = True
                        break
                if flag == False: return flag
    return True

if __name__ == '__main__':
    list = [0]
    flag = canJump(list)
    print(flag)