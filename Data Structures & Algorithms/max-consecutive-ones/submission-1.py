class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = 0
        currOnes = 0
        for n in nums:
            if n == 1:
                currOnes+=1
                maxOnes = max(maxOnes, currOnes)
            else:
                currOnes = 0
        return maxOnes


        