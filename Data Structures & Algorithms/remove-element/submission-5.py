class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        for r in range(len(nums)):
            # if num[r] equals to val, we skip over it 
            # and go until we don't match so we can replace the val
            if nums[r] != val:
                nums[l] = nums[r]
                l+=1
        return l 