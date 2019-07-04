class Solution:
    def isValid(self, s: str) -> bool:
        # https://leetcode.com/problems/valid-parentheses/
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