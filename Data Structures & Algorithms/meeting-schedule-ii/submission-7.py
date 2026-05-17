import heapq

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([interval.start for interval in intervals])
        end = sorted([interval.end for interval in intervals])

        max_meetings = 0
        count = 0
        s = 0
        e = 0

        print(start)
        print(end)

        while s < len(intervals):
            if end[e] > start[s]:
                count += 1
                s += 1
                max_meetings = count if count > max_meetings else max_meetings
            else:
                count -= 1
                e += 1

        return max_meetings
