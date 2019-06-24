class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        https://leetcode.com/problems/game-of-life/
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        R, C = len(board), len(board[0])
        for i in range(R):
            for j in range(C):
                ocount = 0
                for c in [[i-1, j],[i-1, j-1],[i-1, j+1],[i, j-1],[i, j+1],[i+1, j],[i+1, j-1],[i+1, j+1]]:
                    if c[0] < 0 or c[0] >= R or c[1] < 0 or c[1] >= C:
                        continue
                    if board[c[0]][c[1]] >= 1:
                        ocount += 1
                if board[i][j] == 1:
                    if ocount < 2 or ocount > 3: board[i][j] += 1
                else:
                    if ocount == 3: board[i][j] -= 1

        for i in range(R):
            for j in range(C):
                if board[i][j] < 0:
                    board[i][j] = 1
                elif board[i][j] > 1:
                    board[i][j]  = 0