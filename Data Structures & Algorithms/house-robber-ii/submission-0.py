class Solution:
    def rob(self, nums: List[int]) -> int:
        num_hses = len(nums)
        memo1 = {}
        memo2 = {}

        if len(nums) == 1:
            return nums[0]

        return max(
            self.recurRob(nums, 0, memo1, num_hses - 1),
            self.recurRob(nums, 1, memo2, num_hses)
            )

    def recurRob(self, nums, house_idx, memo, end):
        if house_idx >= end:
            return 0

        if house_idx in memo:
            return memo[house_idx]

        memo[house_idx] = max(
            self.recurRob(nums, house_idx + 2, memo, end) + nums[house_idx],
            self.recurRob(nums, house_idx + 1, memo, end)
            )

        return memo[house_idx]
    

