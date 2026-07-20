class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])

        cache = [[-1]*COLS for _ in range(ROWS)]

        def dfs(r,c):
            if r == ROWS or c == COLS:
                return 0
            if r == ROWS-1 and c == COLS-1:
                if obstacleGrid[r][c] != 1:
                    cache[r][c] = 1
                else:
                    cache[r][c] = 0
                
                return cache[r][c]
            if cache[r][c] != -1:
                return cache[r][c]
            # in bounds, not the end, and not in cache

            # make sure its not a 1
            if obstacleGrid[r][c] == 1:
                cache[r][c] = 0
                return cache[r][c]
            
            cache[r][c] = dfs(r+1,c) + dfs(r,c+1)
            return cache[r][c]
        
        return dfs(0,0) if obstacleGrid[0][0] != 1 else 0
            
