class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        dp = {}

        def dfs(i, curr):
            if i == len(stones):
                return curr

            if (i, curr) in dp:
                return dp[(i, curr)]

            # Don't put stones[i] into this group
            skip = dfs(i + 1, curr)

            # Put stones[i] into this group
            take = curr
            if curr + stones[i] <= target:
                take = dfs(i + 1, curr + stones[i])

            dp[(i, curr)] = max(skip, take)
            return dp[(i, curr)]

        best = dfs(0, 0)

        return total - 2 * best