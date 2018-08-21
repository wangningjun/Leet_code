def remove_d(nums):
    nums = set(nums)
    return len(nums)

def main():
    nums = [2, 5, 5, 15]

    a = remove_d(nums)
    print(a)
if __name__ == '__main__':
    main()