import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = []

        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            heapq.heapify(heap)
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            if x != y:
                heapq.heappush(heap, -(x - y))

        return -heap[0] if len(heap) == 1 else 0