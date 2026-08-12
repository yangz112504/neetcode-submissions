class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        currSet = []

        def helper(i,nums,currSet,subsets):
            # if num length reached, append copy of it to totalreslist
            if i >= len(nums):
                subsets.append(currSet.copy())
                return
            # include element
            currSet.append(nums[i])
            helper(i+1, nums, currSet, subsets)
            # make sure to pop to now not include
            currSet.pop()

            helper(i+1, nums, currSet, subsets)
        
        helper(0, nums, currSet, subsets)
        return subsets
                

        