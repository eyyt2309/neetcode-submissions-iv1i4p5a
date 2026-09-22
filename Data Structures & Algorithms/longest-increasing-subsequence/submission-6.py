class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}
        n = len(nums)

        def dfs(i, curr):
            if i == n:
                return 0
            if (i, curr) in dp:
                return dp[(i, curr)]

            skip = dfs(i + 1, curr)
            take = float('-inf')

            if curr < nums[i]:
                take = dfs(i + 1, nums[i]) + 1

            dp[(i, curr)] = max(skip, take)
            return dp[(i, curr)]

        return dfs(0, float('-inf'))