class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}

        def dfs(pos):
            if pos == len(nums) - 1:
                return 0
            elif pos >= len(nums):
                return float('inf')

            if pos in memo:
                return memo[pos]

            min_jump = float('inf')
            for j in range(nums[pos] + 1):
                if j == 0:
                    continue
                else:
                    min_jump = min(dfs(pos + j) + 1, min_jump)

            memo[pos] = min_jump

            return memo[pos]

        return dfs(0)