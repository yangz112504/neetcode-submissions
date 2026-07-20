class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums)-1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        pivotIndex = l

        l = 0
        r = len(nums)-1

        #If the target lies between the smallest element 
        #(pivot) and the last element, then the target 
        #must be inside the right half of the array.
        if target >= nums[pivotIndex] and target <= nums[r]:
            l = pivotIndex
        else:
            r = pivotIndex - 1

        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m -1
        return -1