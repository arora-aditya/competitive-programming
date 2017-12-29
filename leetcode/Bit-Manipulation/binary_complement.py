class Solution(object):
    def findComplement(self, num):
        """
        https://leetcode.com/problems/number-complement/description/
        :type num: int
        :rtype: int
        """
        x_bin="{0:b}".format(num)
        y_bin=""
        for i in x_bin:
            if i=='0':
                y_bin += '1'
            else:
                y_bin += '0'
        return int(y_bin,2)
