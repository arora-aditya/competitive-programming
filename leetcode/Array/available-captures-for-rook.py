class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # https://leetcode.com/problems/available-captures-for-rook/
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'R':
                    r,c = i,j
                    break
        co = 0
        i = r
        while i >= 0:
            if board[i][c] == 'B':
                break
            elif board[i][c] == 'p':
                co += 1
                break
            i -= 1
        i = r
        while i < len(board):
            if board[i][c] == 'B':
                break
            elif board[i][c] == 'p':
                co += 1
                break
            i += 1
        j = c
        while j >= 0:
            if board[r][j] == 'B':
                break
            elif board[r][j] == 'p':
                co += 1
                break
            j -= 1
        j = c
        while j < len(board[0]):
            if board[r][j] == 'B':
                break
            elif board[r][j] == 'p':
                co += 1
                break
            j += 1
        return co
