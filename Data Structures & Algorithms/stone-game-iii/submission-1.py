class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = {}
        n = len(stoneValue)

        def dfs(turn, i):
            if i >= n:
                return 0
            if (turn, i) in dp:
                return dp[(turn, i)]

            # if turn == 1, alice turn else bob
            if turn:
                stones = float('-inf')
                curr = 0
                for j in range(i, min(i + 3, n)):
                    curr += stoneValue[j]
                    stones = max(
                        stones,
                        curr + dfs(False, j + 1)
                    )
            else:
                stones = float('inf')
                curr = 0
                for j in range(i, min(i + 3, n)):
                    curr -= stoneValue[j]
                    stones = min(
                        stones,
                        curr + dfs(True, j + 1)
                    )
            dp[(turn, i)] = stones
            return stones

        score = dfs(True, 0)
        if score > 0:
            return "Alice"
        elif score < 0:
            return "Bob"
        else:
            return "Tie"