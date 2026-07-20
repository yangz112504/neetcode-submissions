class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        # first glance what i'm thinking is that we need a heap. should be a min heap
        # we want to store the distances in the heap, but how are we going to store the coordinates then
        # we can use a tuple (x1,x2,distance) in the heap
        pointsArray = []
        for x,y in points:
            distance = (math.sqrt((x)**2 + (y)**2))
            pointsArray.append((distance, [x,y]))
        
        heapq.heapify(pointsArray)
        
        for i in range(k):
            _, points = heapq.heappop(pointsArray)
            res.append(points)
        return res