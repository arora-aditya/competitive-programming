class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
        dp = [-1]*(len(arr)+1)
        dp[len(arr) - 1] = arr[-1]
        for i in range(len(arr) - 2, -1, -1):
            dp[i] = max(dp[i+1], arr[i])
        return dp[1:]