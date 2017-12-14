class Solution(object):
    def isPalindrome(self, x):
        """
        https://leetcode.com/problems/palindrome-number/description/
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]
