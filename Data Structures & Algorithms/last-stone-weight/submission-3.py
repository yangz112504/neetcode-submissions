class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """Push stones into a maxheap, take the last 2 out, and pop the remainder
        back onto the heap if not 0. do while len > 1 """
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -stone)

        while len(max_heap) > 1:
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)
            if x == y:
                continue
            else:
                heapq.heappush(max_heap, -abs(y-x))
        if len(max_heap) == 1:
            return -max_heap[0]
        else:
            return 0

        