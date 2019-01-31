class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lens = len(nums)
        if lens <= 1:
            return
        initial = k % lens
        i = initial
        start = 0
        temp = nums[start]
        for j in range(lens):
            nums[i], temp = temp, nums[i]
            i = (i+k) % lens
            if i == initial:
                initial = (initial + 1) % lens
                i = initial
                start = (start + 1) % lens
                temp = nums[start]

s = [7,1,2,3,4,5,6]
k = 3
d = Solution()
print(d.rotate(s, k))