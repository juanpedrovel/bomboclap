class Solution:
    def moveZeroes(self, nums):
        lens = len(nums)
        i = 0
        changes = 0
        while i < lens - changes:
            if nums[i] == 0:
                nums.append(nums.pop(i))
                i -= 1
                changes += 1
            i += 1
                
time = [0, 1, 0, 3, 12]
d = Solution()
print(d.moveZeroes(time))
