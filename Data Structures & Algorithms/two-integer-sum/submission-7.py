class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #idea is to keep track of seen numbers in a hashmap
        # so if we encounter a seen number we return both of the indexes,
        #first the seen number(bc smaller index) and then second number
        hashmap = {}
        for index, number in enumerate(nums):
            diff = target - number
            if diff in hashmap:
                return [hashmap[diff], index]
            else:
                hashmap[number] = index
        return 0
        