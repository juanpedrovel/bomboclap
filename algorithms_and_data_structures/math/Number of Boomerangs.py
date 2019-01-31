class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        result = 0
        for x1, y1 in points:
            table = {}
            for x2, y2 in points:
                if x1 == x2 and y1 == y2:
                    continue
                distance = (x1 - x2)**2 + (y1 - y2)**2
                table[distance] = table.get(distance, 0) + 1
            for value in table.values():
                result += value*(value - 1)
        return result

time = 'eceba'
k = 2
d = Solution()
print(d.lengthOfLongestSubstringKDistinct(time, k))
