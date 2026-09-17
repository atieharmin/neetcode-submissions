import numpy as np
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board = np.array(board)
        for row in board:
            filled_row = row[row != "."]
            if len(set(filled_row)) != len(filled_row):
                return False
        columns = board.T
        for column in columns:
            filled_column = column[column != "."]
            if len(set(filled_column)) != len(filled_column):
                return False
        squares = board.reshape(3,3,3,3).swapaxes(1,2).reshape(9, 9)
        for square in squares:
            filled_square = square[square != "."]
            if len(set(filled_square)) != len(filled_square):
                    return False
        return True
