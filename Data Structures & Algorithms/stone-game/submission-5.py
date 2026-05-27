class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        def dfs(turn, piles):
            if len(piles) == 0:
                return 0

            if (turn, tuple(piles)) in memo:
                return memo[(turn, tuple(piles))]

            front = piles[0]
            end = piles[-1]

            if turn % 2 == 0: # alice turn
                memo[(turn, tuple(piles))] = max(dfs(turn + 1, piles[1:]) + front, dfs(turn + 1, piles[:-1]) + end)
            elif turn % 2 == 1: #bob turn
                memo[(turn, tuple(piles))] = min(dfs(turn + 1, piles[1:]), dfs(turn + 1, piles[:-1]))

            return memo[(turn, tuple(piles))]

        dfs(0, piles)
        total = sum(piles)
        bob = total - memo[(0, tuple(piles))]

        if memo[(0, tuple(piles))] > bob:
            return True
        else:
            return False


