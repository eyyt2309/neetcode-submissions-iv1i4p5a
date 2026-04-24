from _heapq import heappop
import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        sorted_intervals = sorted(intervals, key=lambda x: x[0])

        ans = []


        for query in queries:
            heap = []

            for interval in intervals:
                if interval[0] <= query:
                    heapq.heappush(heap,(interval[1] - interval[0] + 1, interval[0], interval[1])) 

            while heap and heap[0][2] < query:
                heappop(heap)
            if not heap:
                ans.append(-1)
            else:
                ans.append(heap[0][0])

        return ans