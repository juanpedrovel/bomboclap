class Solution:
    def spiralOrder(self, matrix):
        self.matrix = matrix
        self.height = len(matrix) - 1
        self.lenght = len(matrix[0])
    
        self.i = 0
        self.j = 0
        self.result = []
        self.counter = len(matrix) * len(matrix[0])
        while self.counter > 0:
            self.right()
            self.i += 1
            self.lenght -= 1
            self.down()
            self.j -= 1
            self.height -= 1
            self.left()
            self.i -= 1
            self.lenght -= 1
            self.up()
            self.j += 1
            self.height -= 1
        return self.result
    
    def right(self):
        if self.counter <= 0:
            return
        for x in range(self.lenght):
            self.result.append(self.matrix[self.i][self.j])
            self.counter -= 1
            self.j += 1
        self.j -= 1
        return
    
    def left(self):
        if self.counter <= 0:
            return
        for x in range(self.lenght):
            self.result.append(self.matrix[self.i][self.j])
            self.counter -= 1
            self.j -= 1
        self.j += 1
        return
    
    def down(self):
        if self.counter <= 0:
            return
        for x in range(self.height):
            self.result.append(self.matrix[self.i][self.j])
            self.counter -= 1
            self.i += 1
        self.i -= 1
        return
    
    def up(self):
        if self.counter <= 0:
            return
        for x in range(self.height):
            self.result.append(self.matrix[self.i][self.j])
            self.counter -= 1
            self.i -= 1
        self.i += 1
        return

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
d = Solution()
print(d.spiralOrder(matrix))