class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        index = 0
        cache = {}
        def cost_helper(index):
            if index > len(cost)-1:
                return 0
            if index in cache:
                return cache[index]
            cache[index] = min(cost[index] + cost_helper(index+1), cost[index] + cost_helper(index+2))
            return cache[index]
        return min(cost_helper(index), cost_helper(index+1))
        