class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * (n+1)

        def helper(i):
            if i == 0 or i == 1:
                return 1
            if i < 0:
                return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] = helper(i-1) + helper(i-2)
            return cache[i]
        
        return helper(n)
        