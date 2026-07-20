class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currMax = 0
        currMin = 0
        globMax = nums[0]
        globMin = nums[0]
        total = 0

        for num in nums:
            currMax = max(currMax+num,num)
            globMax = max(globMax, currMax)
            currMin = min(currMin + num, num)
            globMin = min(globMin, currMin)
            total+=num
        
        if total == globMin: # all negative
            return globMax
        return max(globMax, total-globMin) # either wraparound or contiguous