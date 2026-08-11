class MedianFinder:

    def __init__(self):
        self.large = [] # min heap keep track of all bigger numbers
        self.small = [] # max heap keep track of all smaller numbers
        

    def addNum(self, num: int) -> None:
        # push onto max heap no matter what
        heapq.heappush(self.small, -1*num)
        # if largest value in max heap greater than smallest min heap, move largest to the min heap
        if self.small and self.large and self.small[0]*-1 > self.large[0]:
            val = heapq.heappop(self.small) * -1
            heapq.heappush(self.large,val)
        # check if size in balance
        if len(self.small) > len(self.large) + 1:
            val = heapq.heappop(self.small) * -1
            heapq.heappush(self.large,val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small,val*-1)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0]*-1
        elif len(self.large) > len(self.small):
            return self.large[0]
        else:
            return (self.large[0] + (self.small[0]*-1)) / 2
        
        