class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # well i gotta find the rotten fruits first, get their coordinates
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        # keep track of fresh fruits bc we nede to know if all of them are gone after
        # while loop ends
        freshFruits = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    freshFruits+=1 
                
        # same as initializing 
        minutes = 0
        while len(queue) > 0 and freshFruits > 0:
            for i in range(len(queue)):
                r,c = queue.popleft()
                # we only want to append 1s, so maybe check after for loop
                neighbors = [[0,1], [0,-1], [1,0], [-1,0]]
                for dr,dc in neighbors:
                    if min((r+dr), (c + dc)) < 0 or r + dr == ROWS or c + dc == COLS or grid[r+dr][c+dc] == 2 or grid[r+dr][c+dc] == 0:
                        continue # dont append
                    else: # within boundaries and a 1 and not visited
                        queue.append((r+dr,c+dc))
                        grid[r+dr][c+dc] = 2
                        freshFruits-=1
            minutes+=1
        return minutes if freshFruits == 0 else -1
                