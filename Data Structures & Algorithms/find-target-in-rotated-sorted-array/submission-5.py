class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #finding the min element which is the pivot
        l = 0
        r = len(nums)-1

        while l < r:
            m = (l+r) // 2
            if nums[m] >= nums[r]:
                l = m + 1
            else:
                r = m
        pivot = l

        l = 0
        r = len(nums)-1

        #deciding which sorted half to search

        #if target greater than min and less than pivot's max
        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot -1
        
        while l <= r:
            m = (l + r)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m -1
        return -1
                