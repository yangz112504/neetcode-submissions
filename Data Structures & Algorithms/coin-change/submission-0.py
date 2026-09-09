class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # we can either include the coin or not...

        # table[index][money] holds how many coins you need to make up to the current target amount
        memo = [[-1] * (amount+1) for _ in range(len(coins))]

        def helper(index,currAmount):
            if currAmount == 0:
                return 0
            if index == len(coins):
                if currAmount == 0:
                    return 0
                else:
                    return float('inf')
            if memo[index][currAmount] != -1:
                return memo[index][currAmount]
            
            newCapacity = currAmount - coins[index]
            if newCapacity >= 0:
                memo[index][currAmount] = min(1 + helper(index,newCapacity), helper(index+1, currAmount))
            else:
                memo[index][currAmount] = helper(index+1, currAmount)
            
            return memo[index][currAmount] 
        
        res = helper(0, amount)
        if res == float('inf'):
            return -1
        else:
            return res