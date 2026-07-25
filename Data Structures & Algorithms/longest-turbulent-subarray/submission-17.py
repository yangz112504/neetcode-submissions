class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # Sliding Window
        # increase as long as it's flipping
        # when we stop we move l = r because that stoppage effectively makes sure that is the max subarray up to that stoppage
        l = 0
        maxSize = 1 
        # because all values are positive, we can use addition and subtraction basically to keep track of comparions
        # current - previous. if greater, value is positive, if less, value is negative
        # if 0, auto invalid and move on
        comparisonSign = 0
        for r in range(1, len(arr)):
            currSign = arr[r] - arr[r-1]
            if currSign == 0: # ultimate stop for that portion of array, like right portion isn't gonna be larger bc of left portion
                l = r
            elif (comparisonSign > 0 and currSign > 0) or (comparisonSign < 0 and currSign < 0):
                l = r -1             
            maxSize = max(maxSize, r-l+1)
            comparisonSign = currSign
        return maxSize
        