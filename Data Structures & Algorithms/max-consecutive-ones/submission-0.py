class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = 0
        currOnes = 0
        for n in nums:
            if n == 1:
                currOnes+=1
            else:
                currOnes = 0
            maxOnes = max(maxOnes, currOnes)
        return maxOnes


        