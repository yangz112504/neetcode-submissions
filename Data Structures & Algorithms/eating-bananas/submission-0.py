class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #for a pile of x bananas, it takes ceil(x / k) to eat one pile
        #upper bound of k is the max size of all the piles
        l = 1
        r = max(piles)
        minK = r
        while l <= r:
            mid = (l + r) // 2
            totalHours = 0
            for n in piles:
                totalHours += math.ceil(n / mid)

            if totalHours <= h:
                minK = min(minK, mid)
                r = mid - 1
            else:
                l = mid + 1
        return minK

