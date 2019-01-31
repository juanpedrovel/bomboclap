class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        binary = str(bin(n))[2:]
        for i in binary:
            if i == '1':
                result += 1
        return result

s = 454121
d = Solution()
print(d.hammingWeight(s))