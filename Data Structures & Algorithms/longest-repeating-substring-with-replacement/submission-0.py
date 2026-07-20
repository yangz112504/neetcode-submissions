class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        longestSubstring = 0
        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            #if num replacements > numReplacements we have
            while(r-l+1) - max(count.values()) > k:
                #count of char at left pos and decrement and shift
                count[s[l]]-=1
                l+=1
            longestSubstring = max(longestSubstring, r-l+1)
        return longestSubstring