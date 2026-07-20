import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """Use a max heap with distances calculated by formula
        pop off top k from minheap"""
        def distance(x1,y1):
            x2 = 0
            y2 = 0
            return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

        max_heap = [(-distance(x,y), x, y) for x,y in points]
        heapq.heapify(max_heap)
        while len(max_heap) > k:
            heapq.heappop(max_heap)
        
        res = []
        for _,x,y in max_heap:
            res.append([x,y])
        return res




        