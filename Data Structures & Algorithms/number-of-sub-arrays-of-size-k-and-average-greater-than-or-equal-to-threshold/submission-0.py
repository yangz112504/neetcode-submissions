class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:  
        count = 0
        l = 0
        total = 0
        for r in range(len(arr)):
            if r-l+1 > k:
                total-=arr[l]
                l+=1
            total+=arr[r]

            if r-l+1 == k:
                avg = total/k
                if avg >= threshold:
                    count+=1
        return count
