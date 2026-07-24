import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            if not heap or len(heap) < k:
                heapq.heappush(heap, num)
            else:
                heapq.heappush(heap, num)
                heapq.heappop(heap)

        return heap[0]