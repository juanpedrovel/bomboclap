class Solution:
    def removeDuplicates(self, nums):
        lens = len(nums)
        changes = 0
        i = 0
        while i + changes < lens - 1:
            if nums[i] == nums[i+1]:
                nums.append(nums.pop(i))
                changes += 1
                i -= 1
            i += 1
        return lens - changes
                
time = [0, 1, 0, 3, 12]
d = Solution()
print(d.moveZeroes(time))
