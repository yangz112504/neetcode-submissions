class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalSum = sum(nums)

        if abs(target) > totalSum:
            return 0
        
        if totalSum % 2 != target % 2:
            return 0
        
        # holds num of diff ways a certain combo of index and currSum can build expression to equal target
        cache = {}

        def helper(index, currSum):
            if index == len(nums):
                if currSum == target:
                    return 1
                else:
                    return 0
            if (index,currSum) in cache:
                return cache[(index,currSum)]
            
            cache[(index,currSum)] = helper(index+1,currSum+nums[index]) + helper(index+1, currSum-nums[index])

            return cache[(index,currSum)]
        
        return helper(0,0)


        