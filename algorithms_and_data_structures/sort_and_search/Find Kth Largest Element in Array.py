class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k_largest = len(nums) - k
        
        def partition(l, r):
            j = l
            pivot = nums[l]
            for i in range(l + 1, r + 1):
                if nums[i] <= pivot:
                    j += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[l], nums[j] = nums[j], nums[l]
            return j
        
        left = 0
        right = len(nums) - 1
        while True:
            final_position = partition(left, right)
            if final_position > k_largest:
                right = final_position - 1
            elif final_position < k_largest:
                left = final_position + 1
            else:
                return nums[k_largest]

nums = [3,2,1,5,6,4]
k = 2
d = Solution()
print(d.findKthLargest(nums, k))