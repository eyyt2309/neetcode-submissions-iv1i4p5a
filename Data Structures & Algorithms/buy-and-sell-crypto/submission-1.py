class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(profit, day, coin):
            if day >= len(prices):
                return profit
            
            if (day, coin) in dp:
                return dp[(day, coin)]

            if not coin:
                skip = dfs(profit, day + 1, False)
                buy = dfs(profit - prices[day], day + 1, True)
                max_profit = max(skip, buy)
            else:
                skip = dfs(profit, day + 1, True)
                sell = profit + prices[day]
                max_profit = max(skip, sell)

            dp[day] = max_profit
            return dp[day]

        return dfs(0, 0, False)

        

            


            