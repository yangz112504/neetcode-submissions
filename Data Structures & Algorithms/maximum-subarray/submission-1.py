class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      maxSum = float('-inf')
      currSum = 0
      for i in range(len(nums)):
        currSum+=nums[i]
        maxSum = max(maxSum, currSum)

        #if currSum less than 0 we don't want to keep it so reset to 0
        if currSum < 0:
            currSum = 0
      return maxSum  