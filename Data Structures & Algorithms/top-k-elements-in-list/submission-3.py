class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #get frequency of characters
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        freq = [[] for i in range(len(nums)+1)] #create buckets

        for num, cnt in count.items(): #fill buckets 
            freq[cnt].append(num)
        
        result = [] #extract top k elements starting from k
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result