class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_size = float('inf')
        arr_sum = 0
        left = 0
        for right in range(len(nums)):
            arr_sum += nums[right]

            while arr_sum >= target:
                window_size = min(window_size, right - left + 1)
                arr_sum -= nums[left]
                left += 1

        return 0 if window_size == float('inf') else window_size