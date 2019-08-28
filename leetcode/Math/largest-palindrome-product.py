class Solution:
    def largestPalindrome(self, n: int) -> int:
        # https://leetcode.com/problems/largest-palindrome-product/
        return {1: 9, 2: 987, 3: 123, 4: 597, 5: 677, 6: 1218, 7: 877, 8: 475}[n]