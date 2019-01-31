class Solution:
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def possible(middle):
            # checks how many pairs have lower than middle distance
            # returns True if at least k elements have middle distance
            left = 0
            counter = 0
            for right, number in enumerate(nums):
                while number - nums[left] > middle:
                    left += 1
                counter += right - left
            if counter >= k:
                return True
            return False
        
        nums.sort()
        # does binary search from max possible distance until a distance where
        # only k pairs have lower distance
        max_test_distance = nums[-1] - nums[0]
        min_test_distance = 0
        while min_test_distance < max_test_distance:
            middle = (min_test_distance + max_test_distance) / 2
            if possible(middle):
                max_test_distance = middle
            else:
                min_test_distance = middle + 1
        return int(min_test_distance)

nums = [1,3,1]
k = 1
d = Solution()
print(d.smallestDistancePair(nums, k))