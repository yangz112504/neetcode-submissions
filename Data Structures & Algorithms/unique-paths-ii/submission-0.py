class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 2d dp problem
        # 1 == obstacle, 0 == space
        # need to find a way to stop the search in that path if 1 is encountered
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        cache = [[0]*COLS for i in range(ROWS)]

        def memoization(r,c,cache, obstacleGrid):
            if r == ROWS or c == COLS:
                return 0
            if obstacleGrid[r][c] == 1:
                return 0
            if cache[r][c] > 0:
                return cache[r][c]
            if r == ROWS-1 and c == COLS-1:
                return 1
            cache[r][c] = (memoization(r+1,c,cache,obstacleGrid) + memoization(r,c+1,cache,obstacleGrid))
            return cache[r][c]
        return memoization(0,0,cache,obstacleGrid)
