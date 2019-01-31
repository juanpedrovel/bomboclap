class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not wordDict or not s:
            return False
        word_len = [-1] * len(s)
        for i in range(len(s)):
            if s[:i+1] in wordDict:
                word_len[i] = i+1
            if word_len[i] == -1:
                for j in range(i):
                    if word_len[j] != -1 and s[j+1:i+1] in wordDict:
                        word_len[i] = i - j
                        break
        if word_len[-1] == -1:
            return False
        return True
s = "catsandog"
dict = ["cats","dog","sand","and","cat"]
d = Solution()
print(d.wordBreak(s, dict))