class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        l = 0
        seen = set()
        for r in range(len(s)):
            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l+=1
                    # after finally removing all duplicates
            seen.add(s[r])
            maxLength = max(maxLength, r-l+1)
        return maxLength
        