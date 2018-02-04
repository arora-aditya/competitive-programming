class Solution:
    def isValid(self, s):
        """
        https://leetcode.com/problems/valid-parentheses/description/
        :type s: str
        :rtype: bool
        """
        stack = []
        le = 0
        clos = {"}":"{", ")":"(", "]":"["}
        ope = ("{", "(", "[")
        for i in s:
            if i in ope:
                stack.append(i)
                le += 1
            elif le != 0 and stack[-1] != clos[i]:
                return False
            elif le != 0:
                stack.pop()
                le -=1
            else:
                return False
        return le == 0
