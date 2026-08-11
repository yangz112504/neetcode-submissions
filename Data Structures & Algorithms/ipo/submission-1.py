class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # step 1: have a heap that stores a tuple (capital, profit) normally
        minCapitalHeap = [] # min heap to keep track of capital and profit and can't be empty bc of constraints
        for c,p in zip(capital, profits):
            heapq.heappush(minCapitalHeap,(c, p))
        
        # step 2: for each step from 1 to k, transfer all projects that can be afforded with current capital into temp max heap and then push top project with most profit into w
        maxProfitHeap = []
        for i in range(k):
            while minCapitalHeap and minCapitalHeap[0][0] <= w:
                requiredCapital, profit = heapq.heappop(minCapitalHeap)
                heapq.heappush(maxProfitHeap, -1 * profit)
            if not maxProfitHeap:
                break # no more profit can be earned so return current capital
            w+=(heapq.heappop(maxProfitHeap)*-1) 
        return w

       
        