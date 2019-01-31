from math import log
class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n < 1:
            return False
        x = log(n, 3)
        if 3 ** round(x) == n:
            return True
        return False

s = 243
d = Solution()
print(d.isPowerOfThree(s))