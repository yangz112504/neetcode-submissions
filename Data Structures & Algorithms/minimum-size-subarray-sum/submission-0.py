class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        minLength = float('inf')
        total = 0

        for r in range(len(nums)):
            # add t
            total+=nums[r]
            while total >= target:
                currWindowSize = r-l+1
                minLength = min(minLength, currWindowSize)
                total-=nums[l]
                l+=1
        return 0 if minLength == float('inf') else minLength


        