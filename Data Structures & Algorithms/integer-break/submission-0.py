class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {}

        def dfs(curr):
            if curr == 1:
                return 1
            if curr in dp:
                return dp[curr]

            curr_max = curr # skip breaking
            for i in range(1, curr):
                curr_max = max(curr_max, dfs(i) * dfs(curr - i))

            dp[curr] = curr_max

            return dp[curr]

        ans = 0
        for i in range(1, n):
            ans = max(ans, dfs(i) * dfs(n - i))

        return ans