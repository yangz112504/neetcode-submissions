from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = defaultdict(int)
        l = 0
        longest = 0

        for r in range(len(s)):
            charCount[s[r]]+=1
            maxCharFreq = max(charCount.values())

            while (r-l+1) - maxCharFreq > k:
                charCount[s[l]]-=1
                maxCharFreq = max(charCount.values())
                l+=1
            longest = max(longest,r-l+1)
        
        return longest
            


        