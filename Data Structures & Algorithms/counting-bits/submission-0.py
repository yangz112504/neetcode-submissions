class Solution:
    def countBits(self, n: int) -> List[int]:

        def countOnes(n):
            count = 0
            for i in range(32):
                if 1 & n:
                    count+=1
                n = n>>1
            return count

        output = []
        for i in range(n+1):
            output.append(countOnes(i))
        return output

        