class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = {}
        def dfs(i, curr):
            if curr == amount:
                return 1
            if i < 0:
                return 0
            if (i, curr) in dp:
                return dp[(i, curr)]

            ways = 0
            new_curr = curr
            while new_curr <= amount:
                ways += dfs(i - 1, new_curr)
                new_curr += coins[i]
            dp[(i, curr)] = ways
            return ways

        return dfs(n - 1, 0)