def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    nums = len(strs)
    map = {}
    for i in range(nums):
        key = list(strs[i])
        key.sort()  # key
        key = ''.join(key)

        if key not in map:
            map[key]=[strs[i]]
        else:
            map[key].append(strs[i])
    return map

if __name__ == '__main__':
    strt = ["eat", "tea", "tan", "ate", "nat", "bat"]
    N = groupAnagrams(strt)
    V= list(N.values())
    print(V)

