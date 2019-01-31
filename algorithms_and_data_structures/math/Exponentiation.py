class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1/x
            n = -n
        if n == 0:
            return 1
        answer = 1
        while n > 1:
            if n % 2 == 0:
                x = x * x
                n = n / 2
            else:
                answer = x * answer
                x = x * x
                n = (n - 1) / 2
        return x * answer

n = 100
d = Solution()
print(d.countPrimes(n))