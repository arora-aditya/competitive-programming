class Solution(object):
    def reverse(self, x):
        """
        https://leetcode.com/problems/reverse-integer/
        :type x: int
        :rtype: int
        """
        st = str(x)
        if st[0] == "-":
            k = -1 * int(st[::-1][:-1])
            print(k)
            if k < -2147483648:
                return 0
            else:
                return k
        k = int(st[::-1])
        print(k)
        if k > 2147483647:
            return 0
        else:
            return k
