class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        fresh = 0

        # Append all rotten oranges
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    fresh+=1
        
        neighbors = [[0,1], [0, -1], [1,0], [-1,0]]
        minutes = 0
        while queue and fresh > 0:
            for i in range(len(queue)):
                r,c = queue.popleft()
                for dr, dc in neighbors:
                    new_row = r + dr
                    new_col = c + dc
                    if min(new_row, new_col) < 0 or new_row == ROWS or new_col == COLS or grid[new_row][new_col] == 0 or grid[new_row][new_col] != 1:
                        continue
                    # means the one adjacent must be a 1
                    grid[new_row][new_col] = 2
                    queue.append((new_row, new_col))
                    fresh-=1
            minutes+=1
        return minutes if fresh == 0 else -1

