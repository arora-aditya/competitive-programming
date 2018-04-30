class Solution:
    def generatePossibleNextMoves(self, s):
        """
        https://leetcode.com/problems/flip-game/description/
        :type s: str
        :rtype: List[str]
        """
        result = []
        for c in range(len(s)-1):
            res = ""
            if s[c] == s[c+1]:
                if s[c] == "+":
                    res = s[:c]+"--"+s[c+2:]
                    result.append(res)
        return result
