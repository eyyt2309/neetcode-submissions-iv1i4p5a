class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k_largest = 0
        highest = float('inf')

        nums.sort()

        num_len = len(nums)

        for i in range(num_len - 1, -1, -1):
            if nums[i] <= highest:
                highest = nums[i]
                k_largest += 1
                if k_largest == k:
                    return nums[i]