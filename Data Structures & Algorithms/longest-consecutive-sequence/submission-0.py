class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) #convert list to hashset
        longest = 0 #longest sequence

        for n in nums:
            #for each individual number, new sequence starts if n-1 doesn't exist
            if n-1 not in numSet:  
                length = 0 #length of current sequence
                while n + length in numSet: #while there is a consecutive number
                    length+=1
                longest = max(longest, length) #update longest
        return longest