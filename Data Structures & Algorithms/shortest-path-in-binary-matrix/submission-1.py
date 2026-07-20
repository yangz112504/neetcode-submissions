class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        queue = deque()
        queue.append((0,0,1))
        visited.add((0,0))

        neighbors = [ [0,1], [0,-1], [1,0], [-1,0], 
                        [1,1], [-1,-1], [1, -1], [-1,1] ]
        
        # because we can't go through the queue if the start is 1
        if grid[0][0] == 1 or grid[ROWS-1][COLS-1] == 1:
            return -1

        while queue:
            for i in range(len(queue)):
                r, c, length = queue.popleft()
                if r == ROWS-1 and c == COLS - 1:
                    return length
                
                for dr, dc in neighbors:
                    new_row  = r + dr
                    new_col = c + dc
                    if min(new_row, new_col) < 0 or new_row == ROWS or new_col == COLS or (new_row, new_col) in visited or grid[new_row][new_col] == 1:
                        continue
                    queue.append((new_row, new_col, length + 1))
                    visited.add((new_row, new_col))
        return -1

            