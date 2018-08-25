class Solution(object):
    def minPathSum(self, grid):
        """
        https://leetcode.com/problems/minimum-path-sum/description/
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m > 0:
            n = len(grid[0])
        else:
            return 0
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] = grid[i][0] + dp[i-1][0]
        for j in range(1, n):
            dp[0][j] = grid[0][j] + dp[0][j-1]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        return dp[m-1][n-1]
