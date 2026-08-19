class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        minHeap = [[grid[0][0], 0, 0]]
        visited = set()
        minTime = -1
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


        while minHeap:
            time,r,c = heapq.heappop(minHeap)

            if (r,c) in visited:
                continue
            
            visited.add((r,c))
            minTime = max(minTime, time)

            if (r,c) == (ROWS-1,COLS-1):
                return minTime
            
            for dr, dc in directions:
                nr, nc = r+ dr, c+dc

                if min(nr,nc) < 0 or nr == ROWS or nc == COLS:
                    continue
                heapq.heappush(minHeap,[grid[nr][nc],nr,nc])
        return minTime
            

            
                