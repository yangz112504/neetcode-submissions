class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        if s1 == "":
            return s2 == s3
        if s2 == "":
            return s1 == s3


        memo = [[-1]*len(s2) for _ in range(len(s1))]

        def helper(index1,index2,index3):
            if index1 == len(s1):
                return s2[index2:] == s3[index3:]
            if index2 == len(s2):
                return s1[index1:]== s3[index3:]
            if memo[index1][index2] != -1:
                return memo[index1][index2]
            if s1[index1] == s3[index3] and s2[index2] == s3[index3]:
                memo[index1][index2] = helper(index1 + 1, index2, index3+1) or helper(index1,index2+1,index3+1)
            elif s1[index1] == s3[index3]:
                memo[index1][index2] = helper(index1 + 1, index2, index3+1)
            elif s2[index2] == s3[index3]:
                memo[index1][index2] = helper(index1,index2+1,index3+1)
            else: # no match
                memo[index1][index2] = False
            
            return memo[index1][index2]
        
        return helper(0,0,0)


