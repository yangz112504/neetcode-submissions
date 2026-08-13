class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        totalCombos = []
        currCombos = []
        def helper(index,n,k,totalCombos,currCombos):
            if len(currCombos) == k:
                totalCombos.append(currCombos.copy())
                return
            
            for i in range(index,n+1):
                currCombos.append(i)
                helper(i+1,n,k,totalCombos,currCombos)
                currCombos.pop()
        helper(1,n,k,totalCombos,currCombos)
        return totalCombos
        