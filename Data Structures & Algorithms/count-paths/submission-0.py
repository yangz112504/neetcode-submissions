class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 2d dynamic programming problem
        ROWS = m
        COLS = n
        cache = [[0]*COLS for i in range(ROWS)]

        def memoization(r,c,cache):
            if r == ROWS or c == COLS:
                return 0
            if cache[r][c] > 0:
                return cache[r][c]
            if r == ROWS - 1 and c == COLS-1:
                return 1
            cache[r][c] = (memoization(r+1,c,cache) + memoization(r,c+1, cache))
            return cache[r][c]
        return memoization(0,0,cache)
        