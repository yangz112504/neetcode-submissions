class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 0
        while r < len(nums):
            nums[l] = nums[r] # L represents the original individual value
            while r < len(nums) and nums[r] == nums[l]:
                r+=1
            l+=1
        return l
        