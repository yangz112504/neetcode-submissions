class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # take max
        l = 0
        r = len(heights)-1
        maxArea = 0
        while l < r:
            h = min(heights[l],heights[r])
            w = r - l
            maxArea = max(maxArea, h * w)

            if heights[l] > heights[r]:
                r-=1
            elif heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return maxArea
        