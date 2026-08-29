class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # i'm given just coordinates, not cost
        # have to calculate cost on the fly
        n = len(points)
        node = 0
        minCost = [float('inf')] * n
        visited = [False] * n
        edges = 0
        totalCost = 0

        while edges < n - 1:
            visited[node] = True
            nextNode = -1 # baseline
            # update all minCosts and find next Node
            for i in range(n):
                if visited[i]:
                    continue
                currCost = abs(points[i][0] - points[node][0]) + abs(points[i][1] - points[node][1])
                minCost[i] = min(currCost, minCost[i])
                if nextNode == -1 or minCost[i] < minCost[nextNode]:
                    nextNode = i
            totalCost+=minCost[nextNode]
            node = nextNode
            edges+=1
        
        return totalCost
