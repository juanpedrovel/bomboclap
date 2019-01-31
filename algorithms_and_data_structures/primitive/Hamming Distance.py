class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = '{0:032b}'.format(x)
        y = '{0:032b}'.format(y)
        distance = 0
        for i in range(32):
            if x[i] != y[i]:
                distance += 1
        return distance

x = 1
y = 4
d = Solution()
print(d.hammingDistance(x, y))