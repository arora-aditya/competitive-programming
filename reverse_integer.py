def reverse(x):
    """
    https://leetcode.com/problems/reverse-integer/#/description
    :type x: int
    :rtype: int
    """
    if x > 0:
        y=(x%10)
        flag=1
    elif x < 0:
        x=-1*x
        y=x%10
        flag=-1
    else:
        return 0
    y=y*10
    x=int(x/10)
    i=1
    while x>0:
        y += x%10
        x = int(x/10)
        y = y*10
    if y/10 > 2147483647:
        return 0
    else:
        return int(y*flag/10)

print(reverse(-2147483412))

        
