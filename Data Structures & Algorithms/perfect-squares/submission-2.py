class Solution:
    def numSquares(self, n: int) -> int:
        dp = {}

        def dfs(curr, number):
            if curr == n: # found 1 possible ans
                return number
            if curr in dp:
                return dp[curr]

            min_number = float('inf')

            for i in range(int((n - curr) ** 0.5), 0, -1):
                if (curr + i * i) <= n:
                    min_number = min(min_number, dfs(curr + i * i, number + 1))

            dp[curr] = min_number

            return dp[curr]

        return dfs(0, 0)