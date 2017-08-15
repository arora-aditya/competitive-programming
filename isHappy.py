def isHappy(n):
    """
    https://leetcode.com/problems/happy-number
    :type n: int
    :rtype: bool
    """

    def sumOf(lst):
        sumOf=0
        for i in lst:
            sumOf += (i**2)
        print(sumOf,lst)
        return sumOf
    lst = [int(i) for i in str(n)]
    n=sumOf(lst)
    while n >= 10:
        lst = [int(i) for i in str(n)]
        n = sumOf(lst)
    if n==1 or n==7:
        return True
    return False

print(isHappy(1111111))
