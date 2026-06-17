class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        num_sum = sum(nums)

        memo = {}

        def dfs(pos, total):
            if total == num_sum / 2:
                return True
            if pos == len(nums):
                return False

            if (pos, total) in memo:
                return memo[(pos, total)]

            memo[(pos, total)] = dfs(pos + 1, total + nums[pos]) or dfs(pos + 1, total)
            return memo[(pos, total)]

        return dfs(0, 0)