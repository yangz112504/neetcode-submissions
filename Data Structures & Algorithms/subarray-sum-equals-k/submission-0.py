class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        currSum = 0
        counter = {0:1}

        for num in nums:
            currSum+=num
            diff = currSum - k

            result += counter.get(diff,0)

            counter[currSum] = counter.get(currSum,0)+1
        
        return result


        