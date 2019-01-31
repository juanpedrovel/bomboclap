class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def bx_numb(i, j):
            box_number = 0
            if j > 5:
                box_number += 2
            elif j > 2:
                box_number += 1
            if i > 5:
                box_number += 6
            elif i > 2:
                box_number += 3
            return box_number
        
        
        column = []
        row = []
        box = []
        for i in range(9):
            column.append({})
            row.append({})
            box.append({})
        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell == '.':
                    continue
                else:
                    box_number = bx_numb(i, j)
                    if cell not in column[i] and cell not in row[j] and cell not in box[box_number]:
                        column[i][cell] = 1
                        row[j][cell] = 1
                        box[box_number][cell] = 1
                    else:
                        return False
        return True

s = [
      ["5","3",".",".","7",".",".",".","."],
      ["6",".",".","1","9","5",".",".","."],
      [".","9","8",".",".",".",".","6","."],
      ["8",".",".",".","6",".",".",".","3"],
      ["4",".",".","8",".","3",".",".","1"],
      ["7",".",".",".","2",".",".",".","6"],
      [".","6",".",".",".",".","2","8","."],
      [".",".",".","4","1","9",".",".","5"],
      [".",".",".",".","8",".",".","7","9"]
    ]
    
dict = [2,2]
d = Solution()
print(d.isValidSudoku(s))