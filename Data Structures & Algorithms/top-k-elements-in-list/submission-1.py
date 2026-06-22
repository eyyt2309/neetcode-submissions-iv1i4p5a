from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        ans = []

        for num in freq:
            heapq.heappush(heap, (-freq[num], num))

        for _ in range(k):
            _, num = heapq.heappop(heap)
            ans.append(num)

        return ans