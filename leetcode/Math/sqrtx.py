def mySqrt(x):
    """
    https://leetcode.com/problems/sqrtx/description/
    :type x: int
    :rtype: int
    """

    def check(li, num):
        for i in li[-5:]:
            if i != int(num):
                return False
        return True
    li = [None, None, None, None, None, None]
    root = 1
    flag = True
    while True:
        root = 0.5 * (root + (x/root))
        # print(root, check(li, root), li[-5:])
        if check(li, root):
            return int(root)
        li.append(int(root))
print(mySqrt(2147395599))
