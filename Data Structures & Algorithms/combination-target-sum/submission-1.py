class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # all positive, so we can add and if it's over it's over
        totalCombos = []
        currCombos = []
        def helper(index,totalSum,totalCombos,currCombos):
            if index == len(nums):
                return

            if totalSum == target:
                totalCombos.append(currCombos.copy())
                return
            if totalSum > target:
                return
            
            for i in range(index,len(nums)):
                currCombos.append(nums[i])
                helper(i, totalSum + nums[i], totalCombos, currCombos)
                currCombos.pop()
        nums.sort()
        helper(0,0,totalCombos,currCombos)
        return totalCombos

        