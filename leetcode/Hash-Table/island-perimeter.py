class Solution:
    def islandPerimeter(self, grid):
        """
        https://leetcode.com/problems/island-perimeter/description/
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid == []:
            return 0
        su = 0
        dims = {'height':len(grid),'width':len(grid[0])}
        def check(grid, i, j):
            neighbours = {'left':0, 'top':0, 'right':0, 'bottom':0}
            try:
                if j - 1 >= 0:
                    neighbours['left'] = grid[i][j-1]
            except:
                pass
            try:
                neighbours['right'] = grid[i][j+1]
            except:
                pass
            try:
                if i-1 >= 0:
                    neighbours['top'] = grid[i-1][j]
            except:
                pass
            try:
                neighbours['bottom'] = grid[i+1][j]
            except:
                pass
            # print(i, j, 4 - neighbours['left'] - neighbours['right'] - neighbours['bottom'] - neighbours['top'], neighbours)
            return 4 - neighbours['left'] - neighbours['right'] - neighbours['bottom'] - neighbours['top']
        for i in range(dims['height']):
            for j in range(dims['width']):
                # print(i,j,dims)
                if grid[i][j] == 1:
                    su += check(grid, i, j)
        # for i in range(dims['height']):
        #     print(grid[i])
        return su
            
