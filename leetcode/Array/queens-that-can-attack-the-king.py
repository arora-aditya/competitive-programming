class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        # https://leetcode.com/problems/queens-that-can-attack-the-king/
        board = [
            ['-', '-', '-', '-', '-', '-', '-', '-'], 
            ['-', '-', '-', '-', '-', '-', '-', '-'], 
            ['-', '-', '-', '-', '-', '-', '-', '-'], 
            ['-', '-', '-', '-', '-', '-', '-', '-'], 
            ['-', '-', '-', '-', '-', '-', '-', '-'], 
            ['-', '-', '-', '-', '-', '-', '-', '-'], 
            ['-', '-', '-', '-', '-', '-', '-', '-'], 
            ['-', '-', '-', '-', '-', '-', '-', '-']
        ]
        for queen in queens: 
            board[queen[0]][queen[1]] = 'Q'
        board[king[0]][king[1]] = 'K'

        i,j = king
        ans = []
        while i < 8:
            if board[i][j] == 'Q':
                ans.append([i,j])
                break
            i += 1
        i,j = king
        while i >= 0:
            if board[i][j] == 'Q':
                ans.append([i,j])
                break
            i -= 1
        i,j = king
        while j < 8:
            if board[i][j] == 'Q':
                ans.append([i,j])
                break
            j += 1
        i,j = king
        while j >= 0:
            if board[i][j] == 'Q':
                ans.append([i,j])
                break
            j -= 1
        i,j = king
        while j >= 0 and i >= 0:
            if board[i][j] == 'Q':
                ans.append([i,j])
                break
            i -= 1
            j -= 1
        i,j = king
        while j < 8 and i < 8:
            if board[i][j] == 'Q':
                ans.append([i,j])
                break
            i += 1
            j += 1
        i,j = king
        while j >= 0 and i < 8:
            if board[i][j] == 'Q':
                ans.append([i,j])
                break
            i += 1
            j -= 1
        i,j = king
        while j < 8 and i >= 0:
            if board[i][j] == 'Q':
                ans.append([i,j])
                break
            i -= 1
            j += 1
        return ans
        