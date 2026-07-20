class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = float('inf')
        currSum = 0

        l = 0

        for r in range(len(nums)):
            currSum+=nums[r]
            while currSum >= target:
                minLength = min(r-l+1, minLength)
                currSum-=nums[l]
                l+=1
        return minLength if minLength != float('inf') else 0

