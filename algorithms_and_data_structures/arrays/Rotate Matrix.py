class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix[::] = list(zip(*matrix[::-1]))
        for i in range(len(matrix)):
            matrix[i] = list(matrix[i])

s = [
      [ 5, 1, 9,11],
      [ 2, 4, 8,10],
      [13, 3, 6, 7],
      [15,14,12,16]
    ]
d = Solution()
d.rotate(s)
print(s)