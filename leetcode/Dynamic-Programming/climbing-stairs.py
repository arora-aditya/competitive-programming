class Solution(object):
    def climbStairs(self, n):
        """
        https://leetcode.com/problems/climbing-stairs/description/
        :type n: int
        :rtype: int
        """
        n = n + 1
        root5 = pow(5, 0.5)
        result = 1/root5*( pow((1+root5)/2, n) - pow((1-root5)/2, n) )
        return int(result)
