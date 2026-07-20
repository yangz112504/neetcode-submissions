class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        maxFrequency = 0
        maxLength = 0
        for r in range(len(s)):
            count[s[r]]= 1 + count.get(s[r], 0)
            maxFrequency = max(maxFrequency, count[s[r]])

            # our allowance, k, must be <= window size - count of most frequent
            while (r-l+1) - maxFrequency > k:
                count[s[l]]-=1
                l+=1
            maxLength = max(maxLength, r-l+1)
        return maxLength

            