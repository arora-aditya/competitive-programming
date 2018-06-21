class Solution:
    def countBattleships(self, board):
        """
        https://leetcode.com/problems/battleships-in-a-board/description/
        :type board: List[List[str]]
        :rtype: int
        """
        if board:
            shipNumber = 0
            r,c = len(board), len(board[0])
            boardCopy = [[-1 for x in range(c)] for y in range(r)]
            for i in range(r):
                for j in range(c):
                    # print(i,j,shipNumber)
                    if board[i][j] != "X":
                        # print(i,j, "is a .")
                        continue
                    flag = True
                    if j != 0 and boardCopy[i][j-1] != -1:
                        boardCopy[i][j] = boardCopy[i][j-1]
                        flag = False
                        continue
                    if j != c-1 and boardCopy[i][j+1] != -1 and flag:
                        boardCopy[i][j] = boardCopy[i][j+1]
                        flag = False
                        continue
                    if i != r-1 and boardCopy[i+1][j] != -1 and flag:
                        boardCopy[i][j] = boardCopy[i+1][j]
                        flag = False
                        continue
                    if i != 0 and boardCopy[i-1][j] != -1 and flag:
                        boardCopy[i][j] = boardCopy[i-1][j]
                        flag = False
                        continue
                    if flag:
                        boardCopy[i][j] = shipNumber
                        # print(boardCopy)
                        shipNumber += 1
            print(boardCopy)
            return shipNumber
        else:
            return 0
