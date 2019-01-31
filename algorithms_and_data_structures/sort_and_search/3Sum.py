from collections import defaultdict
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def hashing(i,j,z):
            return ' '.join([str(i),str(j),str(z)])

        nums.sort()
        table = defaultdict(list)
        results = []
        check = set()
        for i, number in enumerate(nums):
            table[number].append(i)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                missing = 0 - nums[i] - nums[j]
                if missing in table:
                    if hashing(nums[i],nums[j], missing) in check:
                        continue
                    for z in table[missing]:
                        if z > j :
                            results.append([nums[i],nums[j],nums[z]])
                            check.add(hashing(nums[i],nums[j],nums[z]))
                            break
        return results

nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
d = Solution()
print(d.threeSum(nums))