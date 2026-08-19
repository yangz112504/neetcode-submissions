class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # when would it be possible for nodes to receive signal vs not?
        # 
        # if minheap still has stuff in it return -1?
        adj = {}
        for i in range(1,n+1):
            adj[i] = []
        
        for ui,vi,ti in times:
            adj[ui].append([vi,ti])

        # shortest to do it and then sum it
        shortest = {}
        minHeap = [[0,k]]

        minTime = 0

        while minHeap:
            cost1, node1 = heapq.heappop(minHeap)
            if node1 in shortest:
                continue
            shortest[node1] = cost1
            minTime = max(minTime, cost1)
            
            if len(shortest) == n:
                return minTime
        

            for node2, cost2 in adj[node1]:
                if node2 not in shortest:
                    heapq.heappush(minHeap, [cost1 + cost2,node2])
            
        return -1
        


        