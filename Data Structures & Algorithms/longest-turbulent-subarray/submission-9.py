class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # count represents number of comparsions, not elements. There will always be
        # one more element than total number of comparisons, so return maxCount+1
        currCount = 0 
        maxCount = 0
        sign = 0 # 0 for prev unset, +1 for greater, -1 for less tan

        for i in range(len(arr)-1):
            left = arr[i]
            right = arr[i+1]
            if left > right:
                if sign == 1:
                    currCount = 1
                else:
                    currCount+=1
                sign = 1
            elif left < right:
                if sign == -1:
                    currCount = 1
                else:
                    currCount+=1
                sign = -1
            else:
                currCount = 0
                sign = 0
            maxCount = max(maxCount, currCount)
        return maxCount+1

        