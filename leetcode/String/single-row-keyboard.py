class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        # https://leetcode.com/problems/single-row-keyboard/
        di = {}
        for i, char in enumerate(keyboard):
            di[char] = i
        ans = 0
        pos = 0
        for char in word:
            ans += abs(di[char] - pos)
            pos = di[char]
        return ans