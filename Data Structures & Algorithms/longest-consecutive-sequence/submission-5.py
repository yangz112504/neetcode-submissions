class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        seen = set(nums)
        maxLength = 0

        for n in nums:
            if n-1 not in seen:
                currLength = 1
                while n + 1 in seen:
                    currLength+=1
                    n = n + 1
                maxLength = max(maxLength, currLength)
        
        return maxLength

        