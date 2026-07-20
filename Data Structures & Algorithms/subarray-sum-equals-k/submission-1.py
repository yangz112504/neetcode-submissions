class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        currSum = 0
        counter = {0:1}

        for num in nums:
            currSum+=num

            # kind of like two sum, we are looking for the complement that is
            diff = currSum - k

            # increment result by the number of occurrences
            result += counter.get(diff,0)

            # update counter with number of occurrences
            counter[currSum] = counter.get(currSum,0)+1
        
        return result


        