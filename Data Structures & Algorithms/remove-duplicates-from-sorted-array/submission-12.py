class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 2 pointers, left stays at k-1 basically, so k = left + 1
        # r moves forward and scan, we use L to keep track of what element we currently need to see if we have dupes of
        l = 0
        for r in range(1, len(nums)):
            if nums[r] == nums[l]:
                continue
            else:
                l+=1
                nums[l] = nums[r]
        return l+1
