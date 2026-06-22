class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        start = []
        end = []

        intervals.sort()

        for a, b in intervals:
            start.append(a)
            end.append(b)

        ans = []

        curr_start = start[0]
        curr_end = end[0]

        for i in range(1, len(intervals)):
            if start[i] > curr_end:
                ans.append([curr_start, curr_end])
                curr_start = start[i]
                curr_end = end[i]
            elif end[i] > curr_end:
                curr_end = end[i]
            else:
                continue
        ans.append([curr_start, curr_end])

        return ans