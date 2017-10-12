class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        https://leetcode.com/problems/binary-number-with-alternating-bits/description/
        """
        xBin = "{0:b}".format(n)
        print(xBin)
        Value = xBin[0]
        for i in range(len(xBin)-1):
            if xBin[i] == xBin[i+1]:
                return False                       
        return True
