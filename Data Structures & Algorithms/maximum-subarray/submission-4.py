class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = nums[0]

        for i in range(len(nums)):
            currSum = max(currSum,0) # if number pushed down below 0, reset to 0

            currSum+=nums[i]

            maxSum = max(maxSum, currSum)
        return maxSum

