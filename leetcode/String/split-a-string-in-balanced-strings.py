class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # https://leetcode.com/problems/split-a-string-in-balanced-strings/
        i = 0
        ans = 0
        for move in s:
            if move == 'L':
                i += 1
            if move == 'R':
                i -= 1
            if i == 0:
                ans += 1
        return ans