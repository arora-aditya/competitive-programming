class Solution:
    def canWin(self, s):
        """
        https://leetcode.com/problems/flip-game-ii/description/
        :type s: str
        :rtype: bool
        """
        for i in range(len(s)-1):
            if s[i]+s[i+1] == '++' and not self.canWin(s[:i]+'--'+s[i+2:]):
                return True
        return False
