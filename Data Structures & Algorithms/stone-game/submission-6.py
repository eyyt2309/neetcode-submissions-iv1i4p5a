class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}

        def dfs(pile):
            if not pile:
                return 0
            
            if tuple(pile) in dp:
                return dp[tuple(pile)]

            best = float('-inf')
            left = pile[0]
            right = pile[-1]
            best = max(
                left - dfs(pile[1:]),
                right - dfs(pile[:-1]),
                best
            ) 

            dp[tuple(pile)] = best
            return best

        if dfs(piles) > 0:
            return True
        else:
            return False


