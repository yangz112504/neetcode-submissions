class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # keep a min heap of the largest elements of size k
        min_heap = []
        for n in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, n)
            else:
                if n > min_heap[0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, n)
        return min_heap[0]

