class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # iterate through longer string, so text2, text1 always shorter or equal
        ROWS = len(text1)
        COLS = len(text2)
        cache = [[-1]*COLS for i in range(ROWS)]
        # cache solves the problem of recalculating the length of subsequence at every combo of letters


        #base case? if out of bounds
        def memoization(r,c,cache):
            if r == ROWS or c == COLS:
                return 0
            if cache[r][c] > -1:
                return cache[r][c]
            total = 0
            if text1[r] == text2[c]:
                cache[r][c] = 1 + memoization(r+1,c+1,cache)
            else:
                cache[r][c] = max(memoization(r+1,c,cache), memoization(r,c+1,cache))
            return cache[r][c]
        return memoization(0,0,cache)
            

        