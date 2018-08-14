def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    s_list = list(s)   # 总串
    t_list = list(t)   # 子串
    s_long = len(s_list)
    t_long = len(t_list)
    count = 0
    for i in range(t_long):
        if t_list[i] not in s_list:
            return ''
    begin = end = 0
    old_long = s_long
    for i in range(s_long-1):
        if s_list[i] in t_list:
            begin = i
        else:
            continue
        for j in range(begin+1,s_long):
            end = j
            temp = s[begin:end]
            if


