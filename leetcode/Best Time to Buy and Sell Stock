class Solution:
    
    def maxProfit(self,prices):
        if len(prices) <= 1:
            return 0
        cur = prices[0]
        profit = 0
        for e in prices[1:]:
            if e > cur:
                profit = max(profit,e - cur)
            else:
                cur = e
        return profit
