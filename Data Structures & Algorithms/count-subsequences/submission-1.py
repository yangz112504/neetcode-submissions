class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ROWS = len(s)
        COLS = len(t)
        cache = [[-1]*COLS for _ in range(ROWS)]
        # ALWAYS MOVE S FORWARD BECAUSE WE NEED TO CHECK ANYWAY
        def dfs(index1, index2, s,t):
              # Base cases:
              # If we've matched all of t, we found a valid subsequence
            if index2 == len(t):
                return 1
            # If we've run out of s but haven't finished t, no valid subsequence

            if index1 == len(s):
                return 0
            if cache[index1][index2] != -1:
                return cache[index1][index2]
            
            # Key insight: index2 progressing means we USE a character from s
            # index2 NOT progressing means we SKIP a character from s
            if s[index1] == t[index2]:
                 # Two options:
                # 1. Use this character: move both pointers forward (index2 progresses = we matched)
                # 2. Skip this character: only move in s (index2 stays = we didn't use this char)
                # Add them because both represent distinct subsequences
                cache[index1][index2] = dfs(index1+1,index2+1,s,t) + dfs(index1+1,index2,s,t)
            else:
                # Characters don't match, we must skip this character in s
                cache[index1][index2] = dfs(index1 + 1, index2, s,t)
            
            return cache[index1][index2]
        
        return dfs(0,0,s,t)

            
        