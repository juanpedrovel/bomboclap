class Solution:
    def imageSmoother(self, M):
        self.image = M
        self.height = len(M)
        self.lenght = len(M[0])
        smoother = []
        if self.height == 1 and self.lenght == 1:
            return M
        for i in range(self.height):
            smoother.append([])
            for j in range(self.lenght):
                smoother[i].append([])
                smoother[i][j] = self.average(i , j)
        return smoother
                
    def average(self, i, j):
        neighbors = self.image[i][j]
        counter = 1
        if i > 0:
            neighbors += self.image[i-1][j]
            counter += 1
            if j > 0:
                neighbors += self.image[i-1][j-1]
                counter += 1
            if j < self.lenght - 1:
                neighbors += self.image[i-1][j+1]
                counter += 1
        if i < self.height - 1:
            neighbors += self.image[i+1][j]
            counter += 1
            if j > 0:
                neighbors += self.image[i+1][j-1]
                counter += 1
            if j < self.lenght - 1:
                neighbors += self.image[i+1][j + 1]
                counter += 1
        if j > 0:
            neighbors += self.image[i][j - 1]
            counter += 1
        if j < self.lenght - 1:
            neighbors += self.image[i][j + 1]
            counter += 1
            
        return (neighbors // counter)

time = [[2,3]]
k = 2
d = Solution()
print(d.imageSmoother(time))
