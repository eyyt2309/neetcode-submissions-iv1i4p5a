class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}

        def dfs(nums, i):
            if i == len(nums) - 1:
                return 0
            if i in memo:
                return memo[i]
            best = float('inf')
            for j in range(1, nums[i] + 1):
                if i + j < len(nums):
                    best = min(best, dfs(nums, i + j) + 1)
            memo[i] = best
            return memo[i]

        return dfs(nums, 0)