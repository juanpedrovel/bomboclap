class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        used = set()
        while n != 1:
            used.add(n)
            n = sum([int(i)**2 for i in str(n)])
            if n in used:
                return False
        return True
