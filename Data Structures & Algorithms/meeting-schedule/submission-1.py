"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        start = sorted([i.start for i in intervals])
        end = sorted([e.end for e in intervals])
        
        sIndex = 0
        eIndex = 0

        available = True
        while sIndex < len(intervals):
            if start[sIndex] < end[eIndex]:
                if available == False:
                    return False
                sIndex+=1
                available = False
            else:
                available = True
                eIndex+=1
        return True
