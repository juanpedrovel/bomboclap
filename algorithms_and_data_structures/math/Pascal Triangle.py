class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        pascal = [[1]]
        previous = pascal[0]
        for i in range(1, numRows):
            pascal.append(0)
            result = []
            result.append(1)
            for j in range(len(previous)-1):
                result.append(previous[j]+previous[j+1])
            result.append(1)
            pascal[i] = result
            previous = result
        return pascal

s = "aaabbcc"
dict = ["aaa","aab","bc"]
d = Solution()
print(d.addBoldTag(s, dict))