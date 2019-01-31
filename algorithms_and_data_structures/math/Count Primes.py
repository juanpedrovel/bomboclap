class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        square_n = int(n**(1/2))
        numbers = [1] * n
        for i in range(2, square_n + 1):
            if numbers[i] == 1:
                for j in range(i, int(n/i) +1):
                    try:
                        numbers[i*j] = 0
                    except:
                        break
        return sum(numbers[2:])

n = 100
d = Solution()
print(d.countPrimes(n))