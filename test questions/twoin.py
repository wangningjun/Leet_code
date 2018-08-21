
def twoSum(nums, target):
    n = 0
    b = 0
    while len(nums) != 0:
        a = n
        t = target - nums[0]
        nums.remove(nums[0])
        n = n + 1
        if t in nums:
            b = nums.index(t)
            b = b + n
            break

    return [a, b]

def main():
    nums= [2, 5, 5, 15]
    target = 20
    a = twoSum(nums, target)
    print(a)
if __name__ == '__main__':
    main()