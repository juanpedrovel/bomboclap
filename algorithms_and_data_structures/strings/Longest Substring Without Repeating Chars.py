class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        table = {}
        max_lenght = 0
        index = 0
        for i in range(len(s)):
            if s[i] not in table:
                table[s[i]] = i
            else:
                if i - index > max_lenght:
                    max_lenght = i - index
                index = max(table[s[i]] + 1, index)
                table[s[i]] = i
        max_lenght = max(max_lenght, len(s) - index)
        return max_lenght
time = "abba"
k = 2
d = Solution()
print(d.lengthOfLongestSubstring(time))