from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # i use a minHeap basically
        # minHeap only ever gets to size k, so push and pop

        freq = Counter(nums)
        minHeap = []
        for num,frequency in freq.items():
            heapq.heappush(minHeap, (frequency,num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        res = []
        for item in minHeap:
            res.append(item[1])
        return res



        