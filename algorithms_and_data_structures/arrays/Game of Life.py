from copy import deepcopy

class Solution:
    def gameOfLife(self, board):
        if not board:
            return board
        self.new_board = deepcopy(board)
        self.height = len(board)
        self.lenght = len(board[0])
        for i in range(self.height):
            for j in range(self.lenght):
                board[i][j] = self.neighbors(i, j)
                
    def neighbors(self, i, j):
        neighbors = 0
        if i < self.height - 1:
            neighbors += self.new_board[i+1][j]
            if j > 0:
                neighbors += self.new_board[i+1][j-1]
            if j < self.lenght - 1:
                neighbors += self.new_board[i+1][j+1]
        if i > 0:
            neighbors += self.new_board[i-1][j]
            if j > 0:
                neighbors += self.new_board[i-1][j-1]
            if j < self.lenght - 1:
                neighbors += self.new_board[i-1][j+1]
        if j > 0:
            neighbors += self.new_board[i][j-1]
        if j < self.lenght - 1:
            neighbors += self.new_board[i][j+1]
        
        if self.new_board[i][j] == 1:
            if neighbors < 2 or neighbors > 3:
                return 0
            return 1
        else:
            if neighbors == 3:
                return 1
            return 0

time = [[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]]
k = 2
d = Solution()
d.gameOfLife(time)
print(time)