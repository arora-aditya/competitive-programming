def solve(board):
    """
    https://leetcode.com/problems/surrounded-regions/description/
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    def surround(x,y):
        print(board[x][y])
        try:
            print(board[x-1][y]+board[x+1][y]+board[x][y-1]+board[x][y+1])
            if board[x-1][y]+board[x+1][y]+board[x][y-1]+board[x][y+1] == "XXXX":
                return True
        except:
            True
        return False
    board_matrix=[[True,True,True,True],[True,True,True,True],[True,True,True,True],[True,True,True,True]]
    while board_matrix != [[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False]]:
        height = len(board)
        width = len(board[0])
        flag=0
        for i in range(height):
            if flag != 1:
                for j in range(width):
                    print(board)
                    if board[i][j]=='O':
                        true_false=surround(i,j)
                        if true_false:
                            board[i][j]="X"
                            flag=1
                            board_matrix[i][j]=False
                            break
            else:
                break
    return board
solve(["XXXX","XOOX","XXOX","XOXX"])
