class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1[:m]
        i = 0
        j = 0
        for k in range(n+m):
            if i >= m:
                nums1[k] = nums2[j]
                j += 1
            elif j >= n:
                nums1[k] = nums1_copy[i]
                i += 1
            else:
                if nums1_copy[i] <= nums2[j]:
                    nums1[k] = nums1_copy[i]
                    i += 1
                else:
                    nums1[k] = nums2[j]
                    j += 1

nums1 = [4,5,6,0,0,0]
m = 3
nums2 = [1,2,3]
n = 3
d = Solution()
print(d.merge(nums1, m, nums2, n))