class Solution:
    def firstUniqChar(self, s):
        chars = {}
        for i in s:
            if i in chars:
                chars[i] += 1
            else:
                chars[i] = 1
        for i in range(len(s)):
            if chars[s[i]] == 1:
                return i
        return -1
                
time = s = "leetcode"
d = Solution()
print(d.firstUniqChar(time))
