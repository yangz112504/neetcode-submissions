class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # at each decision we need to either take
        # cost 1, 2 or 3
        # and we want to return min num of dollars i need to trael everyday in given list of days
        # so the state would be min cost at current day index
        # start a new 3 prong recursion only at end of index
        # otherwise, end only when index is len(days)
        # add days[index] + 1,7, or 15
        n = len(days)
        memo = [-1] * len(days)
        def helper(index):
            if index == n:
                return 0
            if memo[index] != -1:
                return memo[index]

            currDay = days[index]

            oneDayPass = costs[0]+helper(index+1)

            nextSevenIndex = index+1
            while nextSevenIndex != n and days[nextSevenIndex] < currDay+7:
                nextSevenIndex+=1
            
            sevenDayPass = costs[1]+helper(nextSevenIndex)

            nextThirtyIndex = index+1
            while nextThirtyIndex != n and days[nextThirtyIndex] < currDay+30:
                nextThirtyIndex+=1

            thirtyDayPass = costs[2]+helper(nextThirtyIndex)

            memo[index] = min(oneDayPass,sevenDayPass,thirtyDayPass)

            return memo[index]
        
        return helper(0)


            

        