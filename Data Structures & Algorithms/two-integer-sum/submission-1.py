class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #use dict of numbers as keys and values as indices
        myDict = {}
        for index, number in enumerate(nums):
            diff = target - number
            if diff in myDict:
                return [myDict[diff], index]
            myDict[number] = index
        return