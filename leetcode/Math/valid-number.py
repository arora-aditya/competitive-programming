class Solution:
    def isNumber(self, s):
        """
        https://leetcode.com/problems/valid-number/description/
        :type s: str
        :rtype: bool
        """
        try:
            float(s)
            return True
        except ValueError:
            return False
