class Solution:
    def countSubstrings(self, s: str) -> int:

        def helper(l,r):
            count = 0
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    count+=1
                else:
                    break
                l-=1
                r+=1
            return count

        numPalindromes = 0
        for i in range(len(s)):
            # odd
            numPalindromes+=helper(i,i)

            # even
            numPalindromes+=helper(i,i+1)
        
        return numPalindromes