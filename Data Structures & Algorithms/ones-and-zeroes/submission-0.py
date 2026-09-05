class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        cache = {}

        # i can only include if subtracting it doesnt go over boundary
        def helper(index, zeroesLeft, onesLeft):
            if index == len(strs):
                return 0

            numZeroes = strs[index].count("0")
            numOnes = strs[index].count("1")
            if (index,zeroesLeft,onesLeft) in cache:
                return cache[(index,zeroesLeft,onesLeft)]

            newZeroes = zeroesLeft - numZeroes
            newOnes = onesLeft - numOnes

            if newZeroes >= 0 and newOnes >= 0:
                cache[(index,zeroesLeft,onesLeft)] = max(1 + helper(index+1,newZeroes, newOnes), helper(index+1,zeroesLeft,onesLeft))
            else:
                cache[(index,zeroesLeft,onesLeft)] = helper(index+1,zeroesLeft,onesLeft)
            
            return cache[(index,zeroesLeft,onesLeft)]
        
        return helper(0,m,n)


            
            

        