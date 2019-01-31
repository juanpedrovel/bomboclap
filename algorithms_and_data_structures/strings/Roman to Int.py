class Solution:
    def romanToInt(self, s):
        translate = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        lens = len(s)
        number = 0
        for i in range(lens-1, -1, -1):
            num = translate[s[i]]
            if i < lens - 1:
                if num < translate[s[i+1]]:
                    number -= num
                    continue
            number += num
        return number
time = 'IX'
k = 2
d = Solution()
print(d.romanToInt(time))