class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # get all identical numbers next to each other
        perms = [[]]
        for n in nums:
            nextPerm = []
            for p in perms:
                for i in range(len(p)+1):
                    pCopy = p.copy()
                    pCopy.insert(i,n)
                    nextPerm.append(pCopy)
                    if i < len(p) and p[i] == n:
                        break
            perms = nextPerm
        return perms

        