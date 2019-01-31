class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        string = str(x)
        if x < 0:
            string = '-' + string[::-1]
            string = string[:-1]
        else:
            string = string[::-1]
        string = int(string)
        if abs(string) > 2**31 -1:
            return 0
        return string

time = -123
k = 2
d = Solution()
print(d.reverse(time))