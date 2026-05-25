class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def dfs(i, highest):
            if i == len(nums):
                return 0
            if (i, highest) in memo:
                return memo[(i, highest)]

            skip = dfs(i + 1, highest)

            take = 0

            if nums[i] > highest:
                take = 1 + dfs(i + 1, nums[i])

            memo[(i, highest)] = max(skip, take)
            return memo[(i, highest)]

        return dfs(0, float('-inf'))

            
            