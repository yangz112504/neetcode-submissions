class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # kruskal's  get all edges globally
        n = len(points)
        # build min heap
        minHeap = []
        for i in range(n):
            for j in range(i+1,n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)
                heapq.heappush(minHeap, (cost, i , j))
        
        unionFind = UnionFind(n)
        totalCost = 0
        pointsCounted = 0
        while pointsCounted < n-1: # edges
            cost, point1, point2 = heapq.heappop(minHeap)
            if not unionFind.union(point1,point2):
                continue
            totalCost+=cost
            pointsCounted+=1
        
        return totalCost


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
    
    def find(self,v):
        if self.parent[v] == v:
            return v
        self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
    
    def union(self,a,b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA == rootB:
            return False
        self.parent[rootA] = rootB
        return True

        