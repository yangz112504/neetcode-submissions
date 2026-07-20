class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l <= r:
            m = (l+r) //2
            if(nums[m] == target):
                return m
            
            #left sorted portion
            if(nums[l] <= nums[m]):
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else: #less than middle greater than left
                    r = m -1
            #right sorted portition
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1
            
            


        return -1

                