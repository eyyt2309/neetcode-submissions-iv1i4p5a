class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        removals = 0
        lastNonConflict = intervals[0]
        def conflicts(intervalA, intervalB):
            return (intervalA[0] <= intervalB[0] and intervalA[1] > intervalB[0]) or (intervalB[0] <= intervalA[0] and intervalB[1] > intervalA[0])

        for i in range(1, len(intervals)):
            curr = intervals[i]
            if conflicts(lastNonConflict, curr):
                lastNonConflict = lastNonConflict if lastNonConflict[1] < curr[1] else curr
                removals += 1
            else:
                lastNonConflict = curr

        return removals
