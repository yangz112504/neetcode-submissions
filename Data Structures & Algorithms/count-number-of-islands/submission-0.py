class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        # turn all land squares into 0's so nothing is revisited 
        # and visit all the 1s in the process
        def dfs(grid,r,c):
            if min(r,c) < 0 or r == ROWS or c == COLS or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            dfs(grid, r + 1, c)
            dfs(grid, r - 1, c)
            dfs(grid, r, c + 1)
            dfs(grid, r, c - 1)
            return

        numIslands = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1": 
                # for each land, we perform DFS to find all other lands that are connected to it
                    dfs(grid,r,c)
                    numIslands+=1
        return numIslands


        