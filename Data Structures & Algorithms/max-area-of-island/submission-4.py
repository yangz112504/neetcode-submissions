class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # similar to num islands where we dont wanna necessarily backtrack because
        # we want to keep track of the distinct islands but this time their area

        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        maxArea = 0

        def dfs(r,c):
            if min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visited or grid[r][c] == 0:
                return 0
            visited.add((r,c))
            return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r,c))
        
        return maxArea
                