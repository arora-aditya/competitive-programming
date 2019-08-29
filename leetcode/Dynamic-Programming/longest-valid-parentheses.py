class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        le = len(s)
        dp = [0]*le
        ma = 0
        for i in range(le):
            if s[i] == ')':
                if i > 1 and s[i - 1] == '(':
                    if i > 2:
                        dp[i] = dp[i - 2] + 2
                    else:
                        dp[i] = 2
                elif i - dp[i - 1] - 2 > 0 and s[i - 1] == ')':
                    dp[i] = dp[i-1] + dp[i - dp[i - 1] - 2] + 2
            ma = max(ma, dp[i])
        return ma