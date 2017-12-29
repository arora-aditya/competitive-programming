class Solution(object):
    def hasAlternatingBits(self, n):
        """
        https://leetcode.com/problems/binary-number-with-alternating-bits/description/
        :type n: int
        :rtype: bool
        """
        xBin = "{0:b}".format(n)
        Value = xBin[0]
        for i in range(len(xBin)-1):
            if xBin[i] == xBin[i+1]:
                return False
        return True
