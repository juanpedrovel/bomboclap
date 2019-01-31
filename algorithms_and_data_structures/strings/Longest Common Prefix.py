class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        prefix = strs.pop()
        for string in strs:
            if len(prefix) > len(string):
                prefix = prefix[:len(string)]
            for i in range(len(prefix)):
                if prefix[i] != string[i]:
                    prefix = prefix[:i]
                    break
        return prefix
time = ["flower","flow","flight"]
k = 2
d = Solution()
print(d.longestCommonPrefix(time))