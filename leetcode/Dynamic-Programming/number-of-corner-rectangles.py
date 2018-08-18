class Solution(object):
    def countCornerRectangles(self, grid):
        """
        https://leetcode.com/problems/number-of-corner-rectangles
        :type grid: List[List[int]]
        :rtype: int
        """
        R, C = len(grid), len(grid[0])
        if R == 1 or C == 1:
            return 0
        rs = {}
        for i in range(R):
            rs[i] = set()
            for j in range(C):
                if grid[i][j]:
                    rs[i] |= {j}
        count = 0
        rsl, rows, le = {}, [], 0
        for i in rs:
            rsl[i] = len(rs[i])
            rows.append(i)
            le += 1
        for i in range(le):
            for j in range(i+1, le):
                n = rsl[rows[i]] - len(rs[rows[i]] - rs[rows[j]])
                count += (n * (n-1))/2
        return count
