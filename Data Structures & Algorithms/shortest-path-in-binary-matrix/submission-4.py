class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        if grid[0][0] == 1:
            return -1

        queue = deque()
        queue.append((0,0))
        visited.add((0,0))

        shortestPath = 1 #we start with 1 obviously

        while len(queue) > 0: 
            for i in range(len(queue)): # for each level
                r,c = queue.popleft()
                if r == ROWS-1 and c == COLS-1: # the first one to reach will auto hit this and return shortestpath without me needing to min(x,y) it
                    return shortestPath
                neighbors = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
                for dr,dc in neighbors:
                    if min(r + dr, c + dc) < 0 or r + dr == ROWS or c + dc == COLS or (r+dr,c+dc) in visited or grid[r + dr][c + dc] == 1:
                        continue # dont append
                    else:
                        queue.append((r + dr, c + dc))
                        visited.add((r + dr, c + dc))
            shortestPath+=1

        return -1



