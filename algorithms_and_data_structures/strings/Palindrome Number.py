class Solution:
    def isPalindrome(self, x):
        number = str(x)
        lens = len(number) - 1
        j = lens
        i = 0
        while i < j:
            if number[i] != number[j]:
                return False
            i += 1
            j -= 1
        return True