class Solution:
    def climbStairs(self, n: int) -> int:
        cache = dict()
        def memoization(n, cache):
            if n <=2: #base case
                return n
            if n in cache: #if it's in cache
                return cache[n]
            #new value has to be calculated
            cache[n] = memoization(n-1, cache) + memoization(n-2, cache)
            return cache[n]
        return memoization(n, cache)
