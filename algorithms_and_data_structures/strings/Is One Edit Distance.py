class Solution(object):
    def isOneEditDistance(self, s, t):
        lens = len(s)
        lent = len(t)
        if abs(lens - lent) > 1:
            return False
        i = 0
        j = 0
        while i < lens and j < lent:
            if s[i] != t[j]:
                if s[i+1:] == t[j+1:]:
                    return True
                if s[i:] == t[j+1:]:
                    return True
                if s[i+1:] == t[j:]:
                    return True
                else:
                    return False
            j += 1
            i += 1
        if lens == lent:
            return False
        return True

time = [[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]]
k = 2
d = Solution()
d.gameOfLife(time)
print(time)