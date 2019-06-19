class Solution:
    def parseTernary(self, expression: str) -> str:
        # https://leetcode.com/problems/ternary-expression-parser/
        while len(expression) != 1:
            print(expression)
            i = expression.rindex("?")    # begin with the last '?'.
            tmp = expression[i+1] if expression[i-1] == 'T' else expression[i+3]
            expression = expression[:i-1] + tmp + expression[i+4:]
        return expression