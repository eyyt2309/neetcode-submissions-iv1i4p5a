import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            distance = (x**2 + y**2) ** 0.5
            if not heap:
                heapq.heappush(heap, (-distance, x, y))
            elif len(heap) < k:
                heapq.heappush(heap, (-distance, x, y))
            else:
                heapq.heappush(heap, (-distance, x, y))
                heapq.heappop(heap)

        ans = []

        while heap:
            _, x ,y = heapq.heappop(heap)
            ans.append([x, y])

        return ans