class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = list(filter(lambda x: x != ".", board[i]))
            if len(row) != len(set(row)):
                return False
        columns = [list(row) for row in zip(*board)]
        for i in range(9):
            column = list(filter(lambda x: x != ".", columns[i]))
            if len(column) != len(set(column)):
                return False
        for i in range(0,9,3):
            for j in range(0,9,3):
                square = []
                square.append(board[i][j])
                square.append(board[i+1][j])
                square.append(board[i+2][j])
                square = list(filter(lambda x: x != ".", square))
                if len(square) != len(set(square)):
                    return False
                square.append(board[i][j+1])
                square.append(board[i+1][j+1])
                square.append(board[i+2][j+1])
                square = list(filter(lambda x: x != ".", square))
                if len(square) != len(set(square)):
                    return False
                square.append(board[i][j+2])
                square.append(board[i+1][j+2])
                square.append(board[i+2][j+2])
                square = list(filter(lambda x: x != ".", square))
                if len(square) != len(set(square)):
                    return False
        return True
        
         
        
