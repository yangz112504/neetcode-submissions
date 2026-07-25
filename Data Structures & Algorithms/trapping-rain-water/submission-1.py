class Solution:
    def trap(self, height: List[int]) -> int:
        # start at both ends maybe?
        l = 0
        r = len(height)-1
        leftMax = height[l]
        rightMax = height[r]
        maxWater = 0

        while l < r:
            # we shift L or R based on the the limiting factor of the height
            # whatever is shorter will be shifted so that the height of the water can only go up to that and not more
            if leftMax < rightMax:
                l+=1
                maxWater += max(0,leftMax - height[l])
                leftMax = max(leftMax, height[l])
            else:
                r-=1
                maxWater += max(0,rightMax - height[r])
                rightMax = max(rightMax, height[r])
        return maxWater

