class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # first glance what i'm thinking is that we need a heap. should be a min heap
        # we want to store the distances in the heap, but how are we going to store the coordinates then
        # we can use a tuple (distance [x,y]) in the heap
        pointsArray = []
        for x,y in points:
            distance = (math.sqrt((x)**2 + (y)**2)) * -1 # actually store max so we can optimize for space
            item = (distance, [x,y])
            if len(pointsArray) < k:
                heapq.heappush(pointsArray, item)
            else:
                if distance * -1 < pointsArray[0][0] * -1: # make sure they're both positive when comparing
                    heapq.heappop(pointsArray)
                    heapq.heappush(pointsArray, item)
        
        res = [[x,y] for _ , [x,y] in pointsArray]
        return res