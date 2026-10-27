class Solution:
    def countSubstrings(self, s: str) -> int:
        
        def expand(left, right):
            total = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                total+=1
                left-=1
                right+=1
            return total

        res = 0
        for i in range(len(s)):
            res+=expand(i,i) # odd
            res+=expand(i,i+1) # even
        return res

