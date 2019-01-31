class Solution:
    def isValid(self, s):
        if not s:
            return True
        lens = len(s)
        checks = {']':'[', ')':'(', '}':'{'}
        stack = []
        for i in s:
            if i == '[' or i == '(' or i == '{':
                stack.append(i)
            elif i in checks:
                if not stack:
                    return False
                last = stack.pop()
                if checks[i] != last:
                    return False
        if stack:
            return False
        return True

time = "A man, a plan, a canal: Panama"
k = 2
d = Solution()
print(d.isPalindrome(time))
