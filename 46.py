
def perm(n):
    list = []
    if len(n)<=1:

        list.append(n)
    else:
        for i, num in enumerate(n):
            new_n = n[:i]+n[i+1:]
            for y in perm(new_n):
                if [num]+y not in list:
                    list.append([num]+y)

    return list




if __name__ == '__main__':
    n = [1, 1, 3]
    list = perm(n)
    print(list)



