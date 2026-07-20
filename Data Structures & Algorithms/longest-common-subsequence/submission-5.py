class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # i'm thinking we can use a 2d grid with row being text1 and column being text2
        # why? this way, we can store the max subsequence at each step
        ROWS = len(text1)
        COLS = len(text2)
        cache = [[-1]*COLS for _ in range(ROWS)]

        # 2 cases, we can either include the current character or not
        def dfs(index1,index2):
            # check if out of bounds
            if index1 >= len(text1) or index2 >= len(text2):
                return 0
            # return if exists
            if cache[index1][index2] != -1:
                return cache[index1][index2]
            
            if text1[index1] == text2[index2]:
                # move forward both strings and add 1 to longest subsequence
                cache[index1][index2] = 1 + dfs(index1+1,index2+1)
            # if not equal, we want the max of both possible traversal routes, either by moving 1 or the other forward
            else:
                cache[index1][index2] = max(dfs(index1+1,index2),dfs(index1,index2+1))
            return cache[index1][index2]
        return dfs(0,0)

        