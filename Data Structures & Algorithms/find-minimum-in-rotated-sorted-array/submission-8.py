class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        res = nums[0]
        while l <= r:
            if nums[l] < nums[r]: # if left less than right
                res = min(res, nums[l])
                break

            # if array not sorted
            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]: # is apart of the left sorted portion
                l = mid + 1
            else:
                r = mid -1
        return res

            
            