class Solution:
    def romanToInt(self, s: str) -> int:
        # https://leetcode.com/problems/roman-to-integer
        if not s:
            return 0
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        su = 0
        for i in range(len(s)-1):
            if roman[s[i]] < roman[s[i+1]]:
                su -= roman[s[i]]
            else:
                su += roman[s[i]]
        return su + roman[s[-1]]