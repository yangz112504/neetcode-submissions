class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        # because increasing order, we can use two pointers to adjust sum
        # decrease r to decrease currSum, increase l to increase currSum
        while l < r:
            currSum = numbers[l] + numbers[r]
            if currSum == target:
                return [l+1,r+1]
            if currSum > target:
                r-=1
            else:
                l+=1
        return -1
        