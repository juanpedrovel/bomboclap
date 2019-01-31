class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        pigs = 0
        while (minutesToTest / minutesToDie + 1) ** pigs < buckets:
            pigs += 1
        return pigs
                

time3 = [[]]
d = Solution()
print(d.mergeTwoLists(time2[0],time2[1]))
