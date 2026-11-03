class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # gotta keep on movin right pointer to check all characters
        # left can stay at the start of potential permutation
        freq = [0] * 26

        # char freq counter
        for c in s1:
            freq[ord(c)-ord('a')]+=1


        l = 0
        for r in range(len(s2)):
            cIndex = ord(s2[r])- ord('a')
            freq[cIndex]-=1

            while freq[cIndex] < 0:
                freq[ord(s2[l])-ord('a')]+=1
                l+=1
            
            # check if window length reached
            if r - l + 1 == len(s1):
                return True
        
        return False


            
        