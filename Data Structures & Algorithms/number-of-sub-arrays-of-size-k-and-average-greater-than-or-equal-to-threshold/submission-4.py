class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        totalSum = sum(arr[:k])
        n = len(arr)
        count = 1 if totalSum / k >= threshold else 0
        for i in range(k,n):
            totalSum = totalSum + arr[i] - arr[i - k]
            if totalSum / k >= threshold:
                count+=1
        return count