class Solution:
    def shortestPalindrome(self, s):
        lens = len(s)
        front = ''
        rev_s = s[::-1]
        for i in range(lens,-1,-1):
            if s[:i] == rev_s[lens - i:]:
                front = rev_s[:lens-i]
                break
        return front + s
                
time = "aacecaaa"
d = Solution()
print(d.shortestPalindrome(time))
