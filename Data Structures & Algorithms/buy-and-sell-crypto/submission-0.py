class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0

        for left in range(len(prices)):
            for right in range(left, len(prices)):
                if prices[right] - prices[left] > profit:
                    profit = prices[right] - prices[left]

        return profit

        