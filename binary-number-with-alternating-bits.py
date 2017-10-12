class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        https://leetcode.com/problems/binary-number-with-alternating-bits/description/
        """
        xBin = "{0:b}".format(n)
        Value = xBin[0]
        for x in xBin:
            if x != Value:
                return False
            if Value == '1':
                Value = '0'
            else:
                Value = '1'                
        return True
