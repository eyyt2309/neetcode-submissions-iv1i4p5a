import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()


        heap = []
        q_order = []
        ans = []

        for i, query in enumerate(queries):
            q_order.append([query, i])

        q_order.sort(key=lambda a: a[0])
        print(q_order)

        for query, order in q_order:
            for start, end in intervals:
                interval_size = end - start + 1
                if start <= query:
                    heapq.heappush(heap, (interval_size, start, end))
            
            while heap and heap[0][2] < query:
                heapq.heappop(heap)

            if not heap:
                ans.append([-1, order])
            else:
                ans.append([heap[0][0], order])
                while heap:
                    heapq.heappop(heap)

        ans.sort(key=lambda a: a[1])
        result = [x[0] for x in ans]

        return result