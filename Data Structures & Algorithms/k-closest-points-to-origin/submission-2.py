import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """Use a max heap with distances calculated by formula
        pop off top k from minheap"""
        def distance(x1,y1):
            x2 = 0
            y2 = 0
            return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

        max_heap = []
        for x,y in points:
            dist = -distance(x,y)
            heapq.heappush(max_heap, (dist, x, y))

        while len(max_heap) > k:
            heapq.heappop(max_heap)
        
        res = []
        for _,x,y in max_heap:
            res.append([x,y])
        return res




        