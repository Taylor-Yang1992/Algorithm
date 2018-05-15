class Solution:
    
    def maxProfit(self,prices):
        if len(prices) <= 1:
            return 0
        r = [0] * len(prices)
        cur = prices[-1]
        for i in range(len(prices) - 2,-1,-1):
            if prices[i] < cur:
                r[i] = max(r[i + 1],cur - prices[i])
            else:
                r[i] = r[i + 1]
                cur = prices[i]
        l = [0] * len(prices)
        cur = prices[0]
        for i in range(1,len(prices)):
            if prices[i] > cur:
                l[i] = max(l[i - 1],prices[i] - cur)
            else:
                l[i] = l[i - 1]
                cur = prices[i] 
        profit = 0
        for i in range(len(prices)):
            if i == 0:
                profit = max(profit,r[i])
            elif i == len(prices) - 1:
                profit = max(profit,l[i])
            else:
                profit = max(profit,l[i] + r[i + 1])
        return profit
