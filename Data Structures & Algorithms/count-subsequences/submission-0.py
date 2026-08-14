class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ROWS = len(s)
        COLS = len(t)
        cache = [[-1]*COLS for _ in range(ROWS)]

        def dfs(index1, index2, s,t):
            if index2 == len(t):
                return 1
            if index1 == len(s):
                return 0
            if cache[index1][index2] != -1:
                return cache[index1][index2]
            
            # they are the same, we can either
            if s[index1] == t[index2]:
                cache[index1][index2] = dfs(index1+1,index2+1,s,t) + dfs(index1+1,index2,s,t)
            else:
                cache[index1][index2] = dfs(index1 + 1, index2, s,t)
            
            return cache[index1][index2]
        
        return dfs(0,0,s,t)

            
        