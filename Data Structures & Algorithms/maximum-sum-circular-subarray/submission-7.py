class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # cases
        # continuuous on left, continuous on right
        # wrap around. to get wrap around sum we just subtract the minimum sum total sum
        # keep track of total sum and minimum sum?

        totalArraySum = 0 # add this no matter what
        currMinSum = 0 # to keep track of curr negative sum
        maxMinSum = nums[0] # to keep track of max negative sum

        currMaxSum = 0
        maxSum = nums[0]

        # whatever elements comprise of minSum should not be added
        for n in nums:
            if currMinSum > 0: # if positive, we just reset to 0 to get the next negative value
                currMinSum = 0
            if currMaxSum < 0:
                currMaxSum = 0

            currMinSum+=n
            currMaxSum+=n

            maxMinSum = min(maxMinSum, currMinSum)
            maxSum = max(maxSum, currMaxSum)
            # when do i add to totalArraySum then?
            totalArraySum+=n

       

        if maxMinSum < 0:
            totalArraySum = totalArraySum - maxMinSum # wrap around
            if totalArraySum == 0:
                return maxSum

        return max(totalArraySum, maxSum)