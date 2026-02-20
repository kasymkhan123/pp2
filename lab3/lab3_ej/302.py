def isUsual(x):
    while x % 2 == 0 :
        x /= 2
    else :
        while x % 3 == 0 :
            x /= 3
        else :
            while x % 5 == 0:
                x /= 5
    return x == 1
n = int(input())
if isUsual(n):
    print('Yes')
else :
    print('No')