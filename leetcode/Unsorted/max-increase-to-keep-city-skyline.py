class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        https://leetcode.com/problems/max-increase-to-keep-city-skyline/description/
        :type grid: List[List[int]]
        :rtype: int
        """
        sky_LR = [max(row) for row in grid]
        sky_UD = [max(col) for col in zip(*grid)]
        total = 0
        for j in range(len(grid)):
            for k in range(len(grid[0])):
                total += min(sky_LR[j], sky_UD[k]) - grid[j][k]
        return total
        
