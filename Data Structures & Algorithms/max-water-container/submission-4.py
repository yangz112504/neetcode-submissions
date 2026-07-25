class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # we want to have max Area
        # area = height * width
        l = 0
        r = len(heights)-1
        # we want to find a the max area, which involves trying all diff bars
        # we can decide which bar (L or R) to move based on if it's the smaller bar than the other
        # because the higher the min bar theoretically the greater the area
        maxArea = -1
        while l < r:
            currArea = min(heights[l],heights[r])*(r-l)
            maxArea = max(maxArea, currArea)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return maxArea




        