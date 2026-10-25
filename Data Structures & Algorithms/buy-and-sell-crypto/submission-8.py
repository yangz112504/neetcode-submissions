class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProfit = -1
        buy = float('inf')
        for price in prices:
            if price < buy:
                buy = price

            currProfit = price - buy
            maxProfit = max(maxProfit, currProfit)
        
        return maxProfit
