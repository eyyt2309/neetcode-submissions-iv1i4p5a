class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(pos, curr):
            if curr != target and pos == len(nums):
                return 0
            elif curr == target and pos == len(nums):
                return 1

            if (pos, curr) in memo:
                return memo[(pos, curr)]

            add = dfs(pos + 1, curr + nums[pos])
            subtract = dfs(pos + 1, curr - nums[pos])

            memo[(pos, curr)] = add + subtract

            return memo[(pos, curr)]

        return dfs(0, 0)