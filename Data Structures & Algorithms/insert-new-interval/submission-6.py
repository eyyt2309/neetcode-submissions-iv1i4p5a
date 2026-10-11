class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0]) # sort by start
        ans = []

        currStart = None
        currEnd = None

        for start, end in intervals:
            if currStart == None and currEnd == None:
                currStart, currEnd = start, end
            elif start > currEnd: # if next interval starts after current ends
                ans.append([currStart, currEnd])
                currStart = start
                currEnd = end
            else:
                currEnd = max(currEnd, end)

        ans.append([currStart, currEnd])
        return ans