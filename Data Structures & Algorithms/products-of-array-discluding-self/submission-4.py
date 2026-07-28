class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # whole premise of productExceptSelf is that the output array has
        # the prefixProduct and postFix product of everything, in it
        res = [1]*len(nums)
        prefix = 1
        for i in range(0, len(nums)):
            res[i]*=prefix
            prefix*=nums[i]

        print(res)
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        return res
            
