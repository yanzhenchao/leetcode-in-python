#1 Create a stack to store numbers

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        #check row
        for i in range(9):
            row = []
            for j in range(9):
                if board[i][j] in row and board[i][j] != '.':
                    return False
                else:
                    row.append(board[i][j])
        #check column
        for j in range(9):
            col = []
            for i in range(9):
                if board[i][j] in col and board[i][j] != '.' :
                   return False
                else:
                    col.append(board[i][j])
        #check square
        for k in range(3):
            for m in range(3):
                square = []
                for i in range(3*k, 3*k+3):
                    for j in range(3*m, 3*m+3):
                        if board[i][j] in square and board[i][j] != '.':
                            return False
                        else:
                            square.append(board[i][j])
        return True

#2 Combine the loops

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        for i in range(9):
            row = []
            col = []
            for j in range(9):
                if (board[i][j] in row and board[i][j] != '.')\
                or (board[j][i] in col and board[j][i] != '.'):
                    return False
                else:
                    row.append(board[i][j])
                    col.append(board[j][i])
        for k in range(3):
            for m in range(3):
                mid = []
                for i in range(3*k, 3*k+3):
                    for j in range(3*m, 3*m+3):
                        if board[i][j] in mid and board[i][j] != '.':
                            return False
                        else:
                            square.append(mid[i][j])
        return True

#3 More complicated. Removing numbers from the stack instead of adding.

class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        for i in range(9):
            row = list('123456789.')
            col = list('123456789.')
            for j in range(9):
                if board[i][j] not in row or board[j][i] not in col:
                    return False
                if board[i][j] != '.':
                    row.remove(board[i][j])
                if board[j][i] != '.':
                    col.remove(board[j][i])
        for k in range(3):
            for m in range(3):
                square = list('123456789.')
                for i in range(3*k, 3*k+3):
                    for j in range(3*m, 3*m+3):
                        if board[i][j] not in square:
                            return False
                        if board[i][j] != '.':
                            square.remove(board[i][j])
        return True
