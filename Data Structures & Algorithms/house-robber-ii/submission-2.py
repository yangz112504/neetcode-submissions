class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        #if there is only one house, we just rob it
        #use two seperate arrays one from [0: len(nums)-2], another from [1: len(nums-1)]
        def rob_linear(subarray): #run it on two different arrays
            cache = {}
            def rob_helper(index):
                if index > len(subarray)-1:
                    return 0
                if index in cache:
                    return cache[index]
                rob = subarray[index]
                cache[index] = max(rob + rob_helper(index+2), rob_helper(index+1))
                return cache[index]
            return rob_helper(0)
        return max(rob_linear(nums[0: len(nums)-1]), rob_linear(nums[1:]))