class Solution(object):
    def hammingWeight(self, n):
        """
        https://leetcode.com/problems/number-of-1-bits/description/
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')
