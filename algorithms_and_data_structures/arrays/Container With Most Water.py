class Solution:
    def maxArea(self, height):
        lens = len(height)
        area = 0
        i = 0
        j = lens - 1
        for k in range(len(height)):
            left = height[i]
            right = height[j]
            if left > right:
                area = max(area, right * (j - i))
                j -= 1
            else:
                area = max(area, left * (j - i))
                i += 1
        return area
            