class Solution(object):
    def hammingDistance(self, x, y):
        """
        https://leetcode.com/problems/hamming-distance/description/
        :type x: int
        :type y: int
        :rtype: int
        """
        x_bin="{0:b}".format(x)
        y_bin="{0:b}".format(y)
        k=max(len(x_bin),len(y_bin))
        x_bin='0'*(k-len(x_bin))+x_bin
        y_bin='0'*(k-len(y_bin))+y_bin
        count=0
        for i in range(k):
            if x_bin[i] != y_bin[i]:
                count += 1
        return count
