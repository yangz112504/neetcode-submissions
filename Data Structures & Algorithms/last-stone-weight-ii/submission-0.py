class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # this problem is basically a problem of getting two piles of stones to be as close as weight as possible to sum(stones)//2
        total = sum(stones)
        target = total // 2 # want to get as close as possible
        cache = {}
        # cache is useful because if we end up at (index,currSum) differently like 1,2,3... 1+2 or just 3 at index 3 we can save work
        def helper(index, currSum):
            if currSum == target:
                return currSum
            if currSum > target:
                return 0
            if index == len(stones):
                return currSum
            
            if (index,currSum) in cache:
                return cache[(index,currSum)]
            
            includeStone = helper(index+1, currSum + stones[index])
            excludeStone = helper(index+1,currSum)

            cache[(index,currSum)] = max(includeStone, excludeStone)

            return cache[(index,currSum)]
        
        maxHalf = helper(0,0)
        return total - maxHalf - maxHalf


        