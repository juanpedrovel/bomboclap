class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        possible_ways = [0,1,2]
        if n < len(possible_ways):
            return possible_ways[n]
        for i in range(3, n + 1):
            possible_ways.append(0)
            possible_ways[i] = possible_ways[i-1] + possible_ways[i - 2]
        return possible_ways[n]

s = "aaabbcc"
dict = ["aaa","aab","bc"]
d = Solution()
print(d.addBoldTag(s, dict))