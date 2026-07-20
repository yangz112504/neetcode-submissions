class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        for r in range(0,len(nums)):
            if nums[r] != val:
                if r >= l: # Handles edge case of when first element != val by including it 
                    nums[l] = nums[r]
                    l+=1
        return l
        