class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def binary_search_rows():
            left = 0
            right = len(matrix) - 1
            while left <= right:
                middle = (left + right) // 2
                if matrix[middle][0] <= target and target <= matrix[middle][-1]:
                    return binary_search(middle)
                elif matrix[middle][0] > target:
                    right = middle - 1
                else:
                    left = middle + 1
            return False
        
        def binary_search(row):
            left = 0
            right = len(matrix[row]) - 1
            while left <= right:
                middle = (left + right) // 2
                if matrix[row][middle] == target:
                    return True
                elif matrix[row][middle] > target:
                    right = middle - 1
                else:
                    left = middle + 1
            return False
        
        if not matrix or not matrix[0]:
            return False
        return binary_search_rows()

matrix = [
    [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
    ]
target = 5
d = Solution()
print(d.searchMatrix(matrix, target))
