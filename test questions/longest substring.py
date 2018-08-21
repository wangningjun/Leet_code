def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if s == '':
        return 0
    if len(list(set(s))) ==1:
        return 1
    num = 2
    begin = 0
    end = 0
    list_s = list(s)
    for i in range(len(s) - 1):
        if list_s[end + 1] in list_s[begin:end + 1]:
            begin = begin + list_s[begin:end + 1].index(list_s[end+1]) + 1
            num = (end - begin + 1) if num < (end - begin + 1) else num
            end = end+1
        else:
            end = end + 1
            num = (end - begin + 1) if num < (end - begin + 1) else num


    return num

if __name__ == '__main__':
    s = "pwwasdfgywwkwelww"
    print lengthOfLongestSubstring(s)