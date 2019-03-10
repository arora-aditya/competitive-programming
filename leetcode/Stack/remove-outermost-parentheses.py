class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        # https://leetcode.com/problems/remove-outermost-parentheses/
        st = []
        a, b = '', ''
        for char in S:
            # print(char, a, b, st)
            if char == '(':
                a += char
                st.append(char)
            else:
                a += ')'
                st.pop()
                if st == []:
                    b += a[1:-1]
                    a = ''
        return b
