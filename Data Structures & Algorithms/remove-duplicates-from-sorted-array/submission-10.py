class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 1. Remove duplicates in place
        # 2. Make sure first k elements of nums contain unique elements
        # 3. Latter elements of array don't matter
        l = 0
        r = 0
        while r < len(nums):
            nums[l] = nums[r]
            while r < len(nums) and nums[r] == nums[l]:
                r+=1
            l+=1
        return l