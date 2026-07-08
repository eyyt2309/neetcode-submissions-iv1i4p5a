import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for weight in stones:
            heapq.heappush(heap, -weight)
        
        while len(heap) >= 2:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            if x == y:
                continue
            elif x > y:
                heapq.heappush(heap, -(x - y))
            elif y > x:
                heapq.heappush(heap, -(y - x))

        if heap:
            return -heapq.heappop(heap)
        else:
            return 0

