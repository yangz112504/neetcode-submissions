class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = [[-1]*len(s) for _ in range(len(s))]

        def helper(l,r):
            if l < 0 or r >= len(s):
                return 0
            if memo[l][r] != -1:
                return memo[l][r]
            
            if s[l] == s[r]:
                length = 1
                if l == r:
                    memo[l][r] = 1 + helper(l-1,r+1)
                else:
                    memo[l][r] = 2 + helper(l-1,r+1)
            else:
                memo[l][r] = max(helper(l-1,r),helper(l,r+1))
            return memo[l][r]
        
        res = 0

        for i in range(len(s)):
            res = max(res,helper(i,i))
            res = max(res,helper(i,i+1))
        
        return res
        

