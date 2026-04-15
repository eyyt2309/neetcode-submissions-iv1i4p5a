from heapq import heapify, heappush, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heap = []
        heapify(heap)

        for num in nums:
            if len(heap) == 0:
                heappush(heap,num)
                heapify(heap)
            elif len(heap) < k:
                heappush(heap,num)
                heapify(heap)
            elif len(heap) == k and num > heap[0]:
                heappop(heap)
                heappush(heap,num)
                heapify(heap)

        return heappop(heap)
        
        
        # k_largest = 0
        # highest = float('inf')

        # nums.sort()

        # num_len = len(nums)

        # for i in range(num_len - 1, -1, -1):
        #     if nums[i] <= highest:
        #         highest = nums[i]
        #         k_largest += 1
        #         if k_largest == k:
        #             return nums[i]