class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # to include or not to include, because partition means i can
        # split it,as long as all elements in array are used
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False
        targetSum = totalSum // 2
        cache = [[-1] * (targetSum + 1) for _ in range(len(nums))]

        def helper(index, currSum):
            if currSum > targetSum:
                return False
            if currSum == targetSum:
                return True
            if index == len(nums):
                return False
            if cache[index][currSum] != -1:
                return cache[index][currSum]
            
            cache[index][currSum] = helper(index+1,currSum+nums[index]) or helper(index+1,currSum)

            return cache[index][currSum]
        
        return helper(0,0)
            
        