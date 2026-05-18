from collections import deque

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort() 
        ans = []
        stack = deque()
        
        for interval in intervals:
            if not stack:
                stack.append(interval)
            elif interval[0] > stack[-1][1]: # interval starts after previous interval ends
                ans.append(stack.pop())
                stack.append(interval)
            elif stack[-1][1] >= interval[0] >= stack[-1][0] and interval[1] > stack[-1][1]: # interval starts during and ends after
                old = stack.pop()
                stack.append([old[0], interval[1]])

        if stack:
            ans.append(stack.pop())

        return ans


        