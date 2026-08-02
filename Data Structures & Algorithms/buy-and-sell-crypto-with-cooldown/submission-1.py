class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        n = len(prices)

        def dfs(day, coin):
            if day >= n:
                return 0
            if (day, coin) in dp:
                return dp[(day,coin)]
            
            if coin:
                sell = prices[day] + dfs(day + 2, 0)
                skip = dfs(day + 1, 1)
                dp[(day, coin)] = max(sell, skip)
            else:
                buy = -prices[day] + dfs(day + 1, 1)
                skip = dfs(day + 1, 0)
                dp[(day, coin)] = max(buy, skip)

            return dp[(day, coin)]

        return dfs(0, 0)
            