import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if not arr:
            return []
        left = 0
        right = len(arr) - 1

        # binary search to find closest to x
        while left < right:
            mid = (left + right) // 2
            if arr[mid] == x:
                break
            elif arr[mid] > x:
                right = mid
            else:
                left = mid + 1

        heap = []

        for i in range(k + 1):
            if i == 0:
                heapq.heappush(heap, (-abs(arr[mid] - x), -arr[mid]))
            else:
                if mid + i < len(arr):
                    heapq.heappush(heap, (-abs(arr[mid + i]  - x), -arr[mid + i]))
                if mid - i >= 0:
                    heapq.heappush(heap, (-abs(arr[mid - i]  - x), -arr[mid - i]))
        print(heap)

        while len(heap) > k:
            heapq.heappop(heap)

        ans = []
        while heap:
            _, num = heapq.heappop(heap)
            ans.append(-num)

        return sorted(ans)