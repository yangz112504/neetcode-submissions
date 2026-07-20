class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """So we want the k-th largest largest element in an array
        so if we keep a min heap the top will be the k-th largest"""
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]
        