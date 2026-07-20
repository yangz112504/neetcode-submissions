class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[l] < prices[r]: #is it profitable
                profit = prices[r]-prices[l]
                maxProfit = max(maxProfit, profit)
            else: # l is greater than r
                l = r
            r+=1
        return maxProfit
