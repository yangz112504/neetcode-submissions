class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        totalSum = sum(arr[:k]) # sum of first k elements in array
        n = len(arr)
        count = 1 if totalSum / k >= threshold else 0
        l = 0
        for r in range(k,len(arr)):
            totalSum+=arr[r]-arr[l]
            if totalSum >= threshold * k: # avoid floating point division by multiplying both sides by k
                count+=1
            l+=1
        return count
