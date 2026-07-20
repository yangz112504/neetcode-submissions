class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        #keep first element because it's gonna be unique no matter what
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l+=1
        return l