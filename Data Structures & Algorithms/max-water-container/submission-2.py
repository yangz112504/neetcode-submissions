class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        maxArea = 0
        while l < r:
            # calculating and updating max area
            width = r-l
            height = min(heights[l],heights[r])
            maxArea = max(maxArea, width*height)
            
            # calculate which way to move the pointers
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return maxArea
