class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l = 0 #sell date
        r = 1 #profit date
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r #shift left all the way to the minimum bc this means r < l
            r+=1
        return maxProfit
        