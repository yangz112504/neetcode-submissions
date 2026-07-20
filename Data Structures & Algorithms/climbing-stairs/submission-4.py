class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = {}

        def helper(n):
            if n < 0:
                return 0
            if n in cache:
                return cache[n]
            if n == 0:
                return 1
            
            cache[n] = helper(n-1) + helper(n-2)
            return cache[n]
        return helper(n)