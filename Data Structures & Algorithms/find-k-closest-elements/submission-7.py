import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []

        for num in arr:
            if len(heap) < k:
                heapq.heappush(heap, (-abs(num - x) ,-num))
            else:
                heapq.heappush(heap, (-abs(num - x), -num))
                heapq.heappop(heap)

        result = [-x for diff, x in heap]
        return sorted(result)