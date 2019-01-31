class Solution:
    def firstMissingPositive(self, nums):
        lens = len(nums) + 1
        check = [False] * lens
        for i in range(len(nums)):
            if 0 <= nums[i] < lens:
                check[nums[i]] = True
        for i in range(1, lens):
            if check[i] == False:
                return i
        return lens
                
time = [1,2,0]
d = Solution()
print(d.firstMissingPositive(time))
