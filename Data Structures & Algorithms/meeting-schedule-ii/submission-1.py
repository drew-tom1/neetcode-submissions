"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        s = 0
        e = 0
        ct = 0
        res = 0
        start = []
        end = []

        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)

        start.sort()
        end.sort()

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                ct += 1
            else:
                e += 1
                ct -= 1
            res = max(res, ct)
        
        return res

        