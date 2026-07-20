class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #start from the back because all of costs upfront depend on the back
        for i in range(len(cost)-3, -1,-1):
            cost[i] += min(cost[i+1], cost[i+2])
        return min(cost[0], cost[1])
    
    # def minCostClimbingStairs(self, cost: List[int]) -> int:
    #     index = 0
    #     cache = {}
    #     def cost_helper(index):
    #         if index > len(cost)-1:
    #             return 0
    #         if index in cache:
    #             return cache[index]
    #         cache[index] = min(cost[index] + cost_helper(index+1), cost[index] + cost_helper(index+2))
    #         return cache[index]
    #     return min(cost_helper(index), cost_helper(index+1))
        