class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        i = 0
        r = len(nums)-1

        def swap(i, j):
            nums[i], nums[j] = nums[j], nums[i]
        while i <= r:
            if nums[i] == 0:
                swap(i,l)
                l+=1
            if nums[i] == 2:
                swap(i,r)
                r-=1
                i-=1 #subtract 1 because we just swapped in an unknown number from right
            i+=1
        return nums
            
                