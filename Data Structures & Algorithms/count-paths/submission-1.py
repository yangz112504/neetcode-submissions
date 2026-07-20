class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[0] * n for _ in range(m)]
        ROWS = m
        COLS = n

        def helper(r,c):
            if r == ROWS or c == COLS:
                return 0
            # cache initially has value of 0 so if its > than 0 it has been visited so check
            if r == ROWS-1 or c == COLS-1:
                return 1 # found unique path
            if cache[r][c] > 0:
                return cache[r][c]
            # in bounds and not in cache and not the end, so go down r+1,c and right r,c+1
            cache[r][c] = helper(r+1,c) + helper(r,c+1)
            return cache[r][c]



        return helper(0,0)        