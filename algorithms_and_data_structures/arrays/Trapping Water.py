class Solution:
    def trap(self, height):
        water = 0
        i = 0
        while i < len(height) - 2:
            if height[i] > 0:
                if height[i + 1] < height[i]:
                    temp = i+1
                    for j in range(i + 2, len(height)):
                        if height[j] > height[temp]:
                            temp = j
                            barrier = min(height[i], height[temp])
                            if height[j] >= height[i]:
                                break
                    if temp != i+1:
                        for z in range(i+1, temp):
                            water += barrier - height[z]
                        i = temp - 1
            i += 1
        return water
time = [4,9,4,5,3,2]
d = Solution()
print(d.trap(time))