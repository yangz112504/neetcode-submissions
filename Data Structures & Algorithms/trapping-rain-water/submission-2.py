class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = height[0]
        rightMax = height[len(height)-1]
        l = 0
        r = len(height)-1

        totalWater = 0

        while l < r:
            if leftMax < rightMax:
                l+=1
                leftMax = max(leftMax, height[l])
            else:
                r-=1
                rightMax = max(rightMax, height[r])
            
            if height[l] < height[r]:
                totalWater+=(min(leftMax,rightMax)-height[l])
            else:
                totalWater+=(min(leftMax,rightMax)-height[r])
        
        return totalWater

            
            



        