class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # we dont want to backtrack ...
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r,c):
            if min(r,c) < 0 or r == ROWS or c == COLS or (r,c) in visited:
                return
            visited.add((r,c))
            if grid[r][c] == '1':
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
            else:
                return

        count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited:
                    if grid[r][c] == str(1):
                        dfs(r,c)
                        count+=1
                    # dont care if grid[r][c] is 0 bc we dont need to do anything with it
        return count



