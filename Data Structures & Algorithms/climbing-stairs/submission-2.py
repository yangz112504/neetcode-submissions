class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: #if there's 1 stair there's 1 way, if there's 2 stairs theres 2 ways
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)