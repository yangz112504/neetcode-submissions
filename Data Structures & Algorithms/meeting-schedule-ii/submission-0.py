"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        sIndex = 0
        eIndex = 0

        currRooms = 0
        maxRooms = 0

        # iterate through start bc every start will need an end so start will always finish first
        while sIndex < len(intervals):
            if start[sIndex] < end[eIndex]:
                sIndex+=1
                currRooms+=1
            else:
                eIndex+=1
                currRooms-=1
            maxRooms = max(maxRooms, currRooms)
        return maxRooms

        