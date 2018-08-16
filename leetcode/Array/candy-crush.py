class Solution(object):
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        board = map(list,zip(*reversed(board)))
        R, C = len(board), len(board[0])
        while True:
            remove = set()
            for i in range(R):
                for j in range(2, C):
                    if board[i][j] != 0 and board[i][j] == board[i][j-1] == board[i][j-2]:
                        remove |= {(i,j), (i,j-1), (i,j-2)}
            for j in range(C):
                for i in range(2, R):
                    if board[i][j] != 0 and board[i][j] == board[i-1][j] == board[i-2][j]:
                        remove |= {(i,j), (i-1,j), (i-2,j)}
            if remove:
                for i,j in remove: board[i][j] = 0
                for i in range(R):
                    count = 0
                    board[i] = [x for x in board[i] if x]
                    board[i].extend([0]*(C - len(board[i])))
            else:
                break
        return list(reversed(map(list,zip(*board))))


S = Solution()
print(S.candyCrush([[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]))
