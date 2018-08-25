class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        https://leetcode.com/problems/unique-paths-ii/description/
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[1]*n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                for ix in range(i,m):
                    dp[ix][0] = 0
                break;
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                for jx in range(j,n):
                    dp[0][jx] = 0
                break;
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]
