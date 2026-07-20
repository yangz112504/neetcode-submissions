class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        maxWater = 0

        while l < r:
            w = r - l
            area = w * min(heights[l], heights[r])
            if area > maxWater:
                maxWater = area
            
            if heights[l] < heights[r]: #we want larger height
                l+=1
            else:
                r-=1
        return maxWater