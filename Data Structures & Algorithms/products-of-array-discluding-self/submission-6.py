class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        so 1 is 48 bc 2*4*6
        2 is 24 because 1 * 4 * 6
        Each num is a product of everything to it's left and right
        So we can do prefix sum and post fix sum
        1 1 2 8
        """
        output = []
        prefix = 1

        for i in range(len(nums)):
            output.append(prefix)
            prefix*=nums[i]
        
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            output[i]*=postfix
            postfix*=nums[i]
        
        return output

        