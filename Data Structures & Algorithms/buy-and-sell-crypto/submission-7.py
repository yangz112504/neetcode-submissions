class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProfit = -1
        buy = float('inf')
        for price in prices:
            if price < buy:
                buy = price

            currProfit = price - buy
            maxProfit = max(maxProfit, currProfit)
        
        if maxProfit < 0:
            return 0
        else:
            return maxProfit
