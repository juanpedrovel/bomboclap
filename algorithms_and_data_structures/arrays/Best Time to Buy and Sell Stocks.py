class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        days = len(prices)
        i = 0
        while i < days - 1:
            if prices[i+1] <= prices[i]:
                i += 1
            else:
                for j in range(i+1, days):
                    if prices[j] < prices[i]:
                        i = j
                        break
                    profit = max(profit, prices[j] - prices[i])
                    if j == days - 1:
                        return profit
        return profit

s = [7,4,5,3,6,4]
d = Solution()
print(d.maxProfit(s))