class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        multiples_three = 'Fizz'
        multiples_five = 'Buzz'
        multiples_three_and_five = 'FizzBuzz'
        result = []
        for i in range(1, n+1):
            if i % 3 == 0:
                if i % 5 == 0:
                    result.append(multiples_three_and_five)
                else:
                    result.append(multiples_three)
            elif i % 5 == 0:
                result.append(multiples_five)
            else:
                result.append(str(i))
        return result

s = 0
d = Solution()
print(d.fizzBuzz(s))