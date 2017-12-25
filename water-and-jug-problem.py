class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        https://leetcode.com/problems/water-and-jug-problem/description/
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        from fractions import gcd
        return z == 0 or x + y >= z and z % gcd(x, y) == 0
        
