class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {} #keep track of numbers and indexes we already seen

        for index, number in enumerate(nums):
            diff = target - number
            if diff in dict:
                return [dict[diff], index]
            else:
                dict[number] = index
        return
