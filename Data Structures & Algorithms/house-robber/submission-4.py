class Solution:
    def rob(self, nums: List[int]) -> int:
        maxMoneyAtHouses = {}

        def helper(houseNum):
            if houseNum >= len(nums):
                return 0
            if houseNum in maxMoneyAtHouses:
                return maxMoneyAtHouses[houseNum]
            
            dontRob = helper(houseNum+1)
            rob = nums[houseNum] + helper(houseNum+2)
            maxMoneyAtHouses[houseNum] = max(rob, dontRob)
            return maxMoneyAtHouses[houseNum]
        
        return helper(0)
            

        