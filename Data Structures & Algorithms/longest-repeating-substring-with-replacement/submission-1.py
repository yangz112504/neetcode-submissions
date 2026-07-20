class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        longest = 0
        l = 0
        for r in range(len(s)):
            #we want to keep track of most frequent char
            count[s[r]] = 1 + count.get(s[r], 0 )

            #if we don't have enough k's to replace chars 
            #in window
            while (r-l+1) - max(count.values()) > k:
                count[s[l]]-=1
                l+=1
            longest = max(longest, r-l+1)
        return longest

