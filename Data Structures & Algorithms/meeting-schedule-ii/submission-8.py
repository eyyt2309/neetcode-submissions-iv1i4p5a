"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        heap = []
        intervals.sort(key=lambda x: x.start)
        rooms = 0
        for interval in intervals:
            if not heap:
                heapq.heappush(heap, (interval.end, interval.start))
                rooms = max(rooms, len(heap))
            else:
                if interval.start >= heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (interval.end, interval.start))
                else:
                    heapq.heappush(heap, (interval.end, interval.start))
                    rooms = max(rooms, len(heap))
        return rooms