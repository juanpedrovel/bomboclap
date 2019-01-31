class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        previous = '1'
        if n == 0:
            return
        
        def current(previous):
            lens = str(len(previous))
            result = lens + previous[0]
            return result
        
        for i in range(2, n + 1):
            out = []
            start = 0
            for j in range(len(previous) - 1):
                if previous[j] != previous[j+1]:
                    out.append(current(previous[start:j+1]))
                    start = j + 1
            out.append(current(previous[start:]))
            previous = ''.join(out)
        return previous

s = 3
d = Solution()
print(d.countAndSay(s))