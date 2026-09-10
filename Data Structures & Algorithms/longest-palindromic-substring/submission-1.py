class Solution:
    def longestPalindrome(self, s: str) -> str:
        # for each char that we need to begin expanding out from
        def helper(l,r):
            maxLongest = (0,0,0)
            while l >= 0 and r < len(s) and s[l] == s[r]:
                newLongest = r-l+1
                maxLongest = max(maxLongest, (newLongest,l,r))
                l-=1
                r+=1
            return maxLongest

        longest = (0,0,0)

        for i in range(len(s)):
            # odd length palindorme
            longest = max(longest, helper(i,i))

            # even length palindrome
            longest = max(longest, helper(i,i+1))
        
        return s[longest[1]:longest[2]+1]

        
        

        