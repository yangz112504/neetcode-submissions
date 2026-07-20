class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights) #min would have to be at least the max value of cargo
        r = sum(weights) #max would be all the cargo

        def canBeShipped(mid):
            #mid is the weight capacity per day
            daysNeeded = 0
            currSum = 0
            for weight in weights:
                if currSum + weight <= mid:
                    currSum+=weight
                else:
                    daysNeeded += 1
                    currSum = weight
            if currSum > 0:
                daysNeeded+=1
            return True if daysNeeded <= days else False

        while l < r:
            mid = (l + r) // 2
            #some function to check if all the packages can be shipped within days
            #if it can, try lower value
            # if it can't, try higher value
            if canBeShipped(mid):
                r = mid
            else:
                l = mid + 1
        return l