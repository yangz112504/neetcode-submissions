class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # to keep track of frequencies
        charCount = {}
        maxLength = 0
        # to keep track of most frequent letter so we dont need to search through {} every time
        maxFreq = 0
        l = 0
        for r in range(len(s)):
            charCount[s[r]] = 1 + charCount.get(s[r],0)
            maxFreq = max(maxFreq, charCount[s[r]])

            # calculate if we have enough replacements
            while (r-l+1) - maxFreq > k:
                # if we dont, close in sliding window by increasing L until valid window
                charCount[s[l]]-=1
                l+=1
            maxLength = max(maxLength, r-l+1)
        return maxLength
            

            
