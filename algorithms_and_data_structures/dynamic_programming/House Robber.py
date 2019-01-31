class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        lens = len(nums)
        if lens > 2:
            nums[2] += nums[0]
        for i in range(3, lens):
            nums[i] += max(nums[i-2], nums[i-3])
        return max(nums)

s = "42"
d = Solution()
print(d.myAtoi(s))