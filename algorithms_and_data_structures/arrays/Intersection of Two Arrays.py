class Solution:
    def intersection(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        len1 = len(nums1)
        len2 = len(nums2)
        result = []
        check = {}
        counter = 0
        i = 0
        j = 0
        while i < len1 and j < len2:
            if nums1[i] == nums2[j]:
                if nums1[i] not in check:
                    check[nums1[i]] = i
                    result.append(nums1[i])
            if nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return result

time = [1]
k = [1]
d = Solution()
print(d.intersection(time, k))
