class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        currBuyPrice = prices[0]
        for i in range(1, len(prices)):
            if prices[i] <= currBuyPrice:
                currBuyPrice = prices[i]
            else:
                profit = prices[i] - currBuyPrice
                maxProfit = max(maxProfit, profit)
        return maxProfit

            
