class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        max_range = nums[0]
        for i in range(1, len(nums)):
            nums[i] = max(nums[i-1] + nums[i], nums[i])
            max_range = max(max_range, nums[i])
        return max_range

s = "42"
d = Solution()
print(d.myAtoi(s))