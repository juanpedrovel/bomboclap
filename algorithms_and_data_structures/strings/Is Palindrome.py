class Solution(object):
    def isPalindrome(self, s):
        if not s:
            return True
        lens = len(s)
        i = 0
        j = lens - 1
        while i < j:
            while not s[i].isalnum():
                i += 1
            while not s[j].isalnum():
                j -= 1
            if s[i].upper() != s[j].upper():
                return False
            i += 1
            j -= 1
        return True

time = "A man, a plan, a canal: Panama"
k = 2
d = Solution()
print(d.isPalindrome(time))
