class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        minHeap = [[grid[0][0], 0, 0]]
        visited = set((0,0))
        minTime = -1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


        while minHeap:
            time,r,c = heapq.heappop(minHeap)

            minTime = max(minTime, time)

            if (r,c) == (ROWS-1,COLS-1):
                return minTime
            
            for dr, dc in directions:
                nr, nc = r+ dr, c+dc

                if min(nr,nc) < 0 or nr == ROWS or nc == COLS or (nr,nc) in visited:
                    continue
                visited.add((nr,nc))
                heapq.heappush(minHeap,[grid[nr][nc],nr,nc])
        return minTime
            

            
                