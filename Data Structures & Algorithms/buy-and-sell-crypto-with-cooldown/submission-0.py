class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # profit[day][coin]
        profit = [[None for _ in range(2)] for _ in range(len(prices))]
        
        self.recurProfit(prices, 0, profit, 0)

        return profit[0][0]

    def recurProfit(self, prices, day, profit, coin):

        if day >= len(prices):
            return 0

        if profit[day][coin] is not None:
            return profit[day][coin]

        if coin:
            # if i have the coin and sell it
            profit[day][coin] = max(prices[day] + self.recurProfit(prices, day + 2, profit, 0), self.recurProfit(prices, day + 1, profit, 1))
        else:
            profit[day][coin] = max(-prices[day] + self.recurProfit(prices, day + 1, profit, 1), self.recurProfit(prices, day + 1, profit, 0))

        return profit[day][coin]