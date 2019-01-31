class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        table = {}
        for i in nums1:
            if i in table:
                table[i] += 1
            else:
                table[i] = 1
        result = []
        for i in nums2:
            if i in table:
                if table[i] > 0:
                    result.append(i)
                    table[i] -= 1
        return result

s = [1, 2, 2, 1]
dict = [2,2]
d = Solution()
print(d.intersect(s, dict))