class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])

        new_intervals = []
        
        prev_start = intervals[0][0]
        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] > prev_end: # if intervals are non-overlapping
                new_intervals.append([prev_start, prev_end])
                prev_start = intervals[i][0]
                prev_end = intervals[i][1]
            else:
                if intervals[i][0] <= prev_end:
                    prev_end = max(intervals[i][1], prev_end)
        
        new_intervals.append([prev_start, prev_end])

        return new_intervals