class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0,0
        for money in nums:
            temp = max(money + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

    # def rob(self, nums: List[int]) -> int:
    #     index = 0
    #     cache = {}
    #     def rob_helper(index):
    #         if index > len(nums)-1:
    #             return 0
    #         if index in cache:
    #             return cache[index]
    #         rob = nums[index] #index +=2
    #         #index+=1
    #         cache[index] =  max(rob + rob_helper(index+2), rob_helper(index+1))
    #         return cache[index]
    #     return rob_helper(index)