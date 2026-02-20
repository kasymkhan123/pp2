def isValid(x):
    isVal = True
    while x > 0 :
        n = x % 10
        if n % 2 != 0:
            isVal = False
            break 
        x //= 10
    return isVal
y = int(input())
if isValid(y):
    print('Valid')
else :
    print('Not valid')

