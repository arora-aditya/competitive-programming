class Solution:
    def projectionArea(self, grid):
        """
        https://leetcode.com/problems/projection-area-of-3d-shapes/description/
        :type grid: List[List[int]]
        :rtype: int
        """
        su = 0
        for i in grid:
            ma = -1
            for j in i:
                if ma < j:
                    ma = j
                if j != 0:
                    su += 1
            su += ma
        # print(su)
        for i in range(len(grid)):
            ma = -1
            for j in range(len(grid[i])):
                # print(grid[j][i])
                if ma < grid[j][i]:
                    ma = grid[j][i]
            # print(ma)
            su += ma
        # print(su)
        return su
