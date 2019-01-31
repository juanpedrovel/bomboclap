class Solution:
    def myAtoi(self, string):
        if not string:
            return 0
        lens = len(string)
        result = []
        negative = False
        i = 0
        while i < lens and string[i] == ' ':
            i += 1
        if i < lens and (string[i] == '-' or string[i] == '+'):
            result.append(string[i])
            i += 1
        while i < lens and string[i].isdigit():
            result.append(string[i])
            i += 1
        if not result or (result == ['-'] or result == ['+']):
            return 0
        answer = int(''.join(result))
        answer = min(answer, 2**31 - 1)
        answer = max(answer, -(2**31))
        return answer

s = "42"
d = Solution()
print(d.myAtoi(s))