class Solution:
    def isPalindrome(self, x: int) -> bool:
        # https://leetcode.com/problems/palindrome-number/
        y = str(x)
        return y == y[::-1]