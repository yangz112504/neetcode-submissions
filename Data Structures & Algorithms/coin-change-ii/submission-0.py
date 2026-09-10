class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # what does the memo table hold
        # how many distinct combos we can make at current amount and current coin how about that
        memo = [[-1]*amount for _ in range(len(coins))]
        n = len(coins)
        def helper(index, currAmount):
            if index == n:
                return 0
            if currAmount > amount:
                return 0
            if currAmount == amount:
                return 1
            
            if memo[index][currAmount] != -1:
                return memo[index][currAmount]
            
            includeCurr = helper(index,currAmount + coins[index])

            exclude = helper(index+1,currAmount)

            memo[index][currAmount] = includeCurr + exclude
            return memo[index][currAmount]
        
        return helper(0,0)
        