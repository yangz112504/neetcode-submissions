class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones) # turn into a maxheap

        while len(stones) > 1:
            x = heapq.heappop(stones)*-1
            y = heapq.heappop(stones) * -1
            if x == y:
                continue
            elif x < y:
                heapq.heappush(stones, (y-x)*-1)
            else:
                heapq.heappush(stones, (x-y)*-1)
        return stones[0]*-1 if stones else 0

        