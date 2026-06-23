class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        global_sum = nums[0]
        curr_sum = nums[0]

        for num in nums[1:]:
            curr_sum = max(num, curr_sum + num)
            if global_sum < curr_sum:
                global_sum = curr_sum

        return global_sum
