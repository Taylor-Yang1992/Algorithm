class Solution:
    
    def maxProfit(self,prices):
        if len(prices) <= 1:
            return 0
        cur = 0
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] >= prices[i - 1]:
                continue
            else:
                profit += (prices[i - 1] - prices[cur])
                cur = i
        if cur < len(prices):
            profit += (prices[-1] - prices[cur])
        return profit           
