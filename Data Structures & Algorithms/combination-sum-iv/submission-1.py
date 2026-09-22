class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        dp = {}

        def dfs(curr):
            if curr == target:
                return 1
            if curr >= target:
                return 0
            if curr in dp:
                return dp[curr]

            total = 0
            for i in range(n):
                total += dfs(curr + nums[i])
            dp[curr] = total
            return total

        return dfs(0)