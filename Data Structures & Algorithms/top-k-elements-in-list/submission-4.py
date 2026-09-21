from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # i use a maxHeap basically
        # maxHeap inputs: (frequency,num)
        freq = Counter(nums)
        maxHeap = []
        for num,frequency in freq.items():
            heapq.heappush(maxHeap, (-frequency,num))
        
        res = []
        for i in range(0,k):
            num = heapq.heappop(maxHeap)[1]
            res.append(num)
        return res



        