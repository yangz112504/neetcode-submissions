class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # i'm given just coordinates, not cost
        # have to calculate cost on the fly
        n = len(points)
        minHeap = []
        # cost, node
        minHeap.append((0,0))
        visited = set() # only stores node
        totalCost = 0

        while len(visited) < n:
            cost, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            
            visited.add(node)

            totalCost+=cost

            for nextNode in range(n):
                if nextNode not in visited:
                    cost = abs(points[node][0]-points[nextNode][0]) + abs(points[node][1] - points[nextNode][1])
                    heapq.heappush(minHeap, (cost,nextNode))
        
        return totalCost
            
            
        

        