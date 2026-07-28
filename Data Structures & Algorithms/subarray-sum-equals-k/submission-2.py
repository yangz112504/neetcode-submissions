class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # key value current prefixSum
        # initial value of 0 because you technically have an empty subarray
        res = 0
        hashmap = {0:1}
        currSum = 0
        for n in nums:
            currSum+=n
            diff = currSum - k # the match for the current number
            if diff in hashmap:
                res+=hashmap[diff]
            hashmap[currSum] = 1 + hashmap.get(currSum,0)
        return res
