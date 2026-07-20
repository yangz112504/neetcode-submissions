class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)
        
        

    def add(self, val: int) -> int:  
        if len(self.heap) < self.k:
            heapq.heappush(self.heap,val)
            return self.heap[0]

        # we only really care about the kth largest elements. So we always want to keep k elements
        kthLargest = self.heap[0]
        if val > kthLargest: #if incoming val is greater than kthLargest, that means we'll have new kth largest so we need to pop
            heapq.heappop(self.heap)
            heapq.heappush(self.heap,val)
        return self.heap[0]

        
