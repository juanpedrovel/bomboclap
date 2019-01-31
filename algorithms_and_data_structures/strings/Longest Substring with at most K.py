class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if not s or not k:
            return 0
        lens = len(s)
        used = {}
        start = 0
        longest = 0
        for i in range(lens):
            char = s[i]
            used[char] = used.get(char, 0) + 1
            while len(used) > k:
                used[s[start]] -= 1
                if used[s[start]] == 0:
                    del used[s[start]]
                start += 1
            longest = max(longest, i+1 - start)
        return longest


time = 'eceba'
k = 2
d = Solution()
print(d.lengthOfLongestSubstringKDistinct(time, k))