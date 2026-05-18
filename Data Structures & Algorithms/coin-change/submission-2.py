class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        memo = {}
        def dfs(amount, num, idx):
            if amount == 0:
                return num
            if amount < coins[-1]:
                return float('inf')
            if idx == len(coins):
                return float('inf')
            if (amount, num, idx) in memo:
                return memo[(amount, num, idx)]
            
            best = float('inf')
            max_coins = (amount // coins[idx])
            for num_coin in range(max_coins + 1):
                best = min(best, dfs(amount - (num_coin * coins[idx]), num + num_coin, idx + 1))
            memo[(amount, num, idx)] = best
            return memo[(amount, num, idx)]

        ans = dfs(amount, 0, 0) 

        return ans if ans != float('inf') else -1
        