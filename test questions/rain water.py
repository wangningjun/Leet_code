def tr_resolve(s):
    if min(s) != s[1]:
        return 0
    else:
        num = min((s[0]-s[1]),s[2]-s[1])
        return num

def trap(height):
    result = 0
    for i in range(len(height)-2):
        result = result + tr_resolve(height[i:i+3])
    return result

if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(trap(height))

