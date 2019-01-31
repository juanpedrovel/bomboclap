class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        lens = len(nums)
        result = lens*(1 + lens) / 2
        for i in nums:
            result -= i
        return int(result)

s = [0]
d = Solution()
print(d.missingNumber(s))