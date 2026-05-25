import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            heapq.heappush(heap, (math.sqrt(pow(point[0], 2)+ pow(point[1], 2)), point))
        ans = []
        for _ in range(k):
            _, point = heapq.heappop(heap)
            ans.append(point)

        return ans