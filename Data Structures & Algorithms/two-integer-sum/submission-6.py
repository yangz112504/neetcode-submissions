class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, number in enumerate(nums):
            diff = target - number
            if diff in hashmap:
                return [hashmap[diff], index]
            hashmap[number] = index
        return []