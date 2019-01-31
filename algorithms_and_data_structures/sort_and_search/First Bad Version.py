def isBadVersion(version):
    versions = [0,1,1]
    return versions[version]

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return
        if n == 1:
            if isBadVersion(n):
                return n
            else:
                return
        start = 1
        end = n
        while start != end:
            half = (start + end) // 2
            if isBadVersion(half) == True:
                end = half
            else:
                if start == half:
                    return end
                start = half
        return start

n = 2
d = Solution()
print(d.firstBadVersion(n))