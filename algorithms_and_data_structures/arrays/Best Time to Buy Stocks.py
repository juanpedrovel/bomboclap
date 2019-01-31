class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        stocks = None
        price = 0
        for i in range(len(prices)):
            if stocks == None:
                if i < len(prices) - 1:
                    if prices[i+1] > prices[i]:
                        stocks = prices[i]
            else:
                if i < len(prices) - 1:
                    if prices[i+1] <= prices[i]:
                        profit += prices[i] - stocks
                        stocks = None
        if stocks != None:
            profit += prices[-1] - stocks
        return profit

prices = [7,1,5,3,6,4]
d = Solution()
print(d.maxProfit(prices))