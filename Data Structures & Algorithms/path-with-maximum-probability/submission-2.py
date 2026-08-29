class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {}
        for i in range(n):
            adj[i] = []
        
        for edge, prob in zip(edges,succProb):
            a, b = edge
            adj[a].append([b,prob])
            adj[b].append([a,prob])
        
        maxHeap = [[-1.0,start_node]]
        visited = set()

        while maxHeap:
            prob, node = heapq.heappop(maxHeap)

            if node in visited:
                continue

            visited.add(node)

            if node == end_node:
                return prob * -1
            
            for node2, prob2 in adj[node]:
                if node2 not in visited:
                    heapq.heappush(maxHeap, [prob2 * prob,node2])
        return 0
            
            

        