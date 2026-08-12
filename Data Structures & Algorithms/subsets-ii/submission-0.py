class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subset = []
        currset = []
        
        def helper(i,nums,currset,subset):
            if i >= len(nums):
                subset.append(currset.copy())
                return
            # include curr number
            currset.append(nums[i])
            helper(i+1,nums,currset,subset)
            currset.pop()
            
            # exclude by skipping over extra curr numbers
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i+=1

            helper(i+1,nums,currset,subset)

        helper(0,nums,currset,subset)

        return subset


        