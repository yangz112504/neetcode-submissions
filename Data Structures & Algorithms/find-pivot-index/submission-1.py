class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rightSum = sum(nums)
        leftSum = 0
        for r in range(len(nums)):
            rightSum-=nums[r]
            if rightSum == leftSum:
                return r
            leftSum+=nums[r]
        return -1