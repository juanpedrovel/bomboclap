import itertools

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        table = {2:['a','b','c'], 3:['d','e','f'], 4:['g','h','i'], 5:['j','k','l'], 6:['m','n','o'], 7:['p','q','r','s'], 8:['t','u','v'],                     9:['w','x','y','z']}
        used = []
        for i in digits:
            used.append(table[int(i)])
        
        result = [list(tup) for tup in list(itertools.product(*used))]
        result = [''.join(element) for element in result]
        return result

#s = "aaabbcc"
#dict = ["aaa","aab","bc"]
#d = Solution()
#print(d.addBoldTag(s, dict))