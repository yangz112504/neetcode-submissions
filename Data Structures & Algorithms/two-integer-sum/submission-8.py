class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in x:
                return [x[diff],index]
            else:
                x[num] = index
        return -1
        