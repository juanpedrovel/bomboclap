class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        len_needle = len(needle)
        first_char_needle = needle[0]
        for i in range(len(haystack) - len_needle + 1):
            if haystack[i] == needle[0]:
                if haystack[i:i+len_needle] == needle:
                    return i
        return -1

s = "a"
dict = "ab"
d = Solution()
print(d.strStr(s, dict))