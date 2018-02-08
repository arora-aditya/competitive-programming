class Solution(object):
    def validPalindrome(self, s):
        """
        https://leetcode.com/problems/valid-palindrome-ii/description/
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                one, two = s[left:right], s[left + 1:right + 1]
                return one == one[::-1] or two == two[::-1]
            left, right = left + 1, right - 1
        return True

        
