class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        # provides O(1) lookup for numbers.
        # a number must be the start of a sequence if x-1 doesnt exist. because if
        # x - 1 does, it's in the middle, that's it!
        maxLength = 0
        for num in hashset:
            if num-1 not in hashset:
                currLength = 0
                while True:
                    if num in hashset:
                        currLength+=1
                        num+=1
                    else:
                        break
                maxLength = max(maxLength, currLength)
        return maxLength

            

        