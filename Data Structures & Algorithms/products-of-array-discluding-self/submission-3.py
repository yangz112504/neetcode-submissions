class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # multiply everything to the right and everything to the left
        output = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            output[i]*=prefix
            prefix*=nums[i]
        
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            output[i]*=postfix
            postfix*=nums[i]
        
        return output




        