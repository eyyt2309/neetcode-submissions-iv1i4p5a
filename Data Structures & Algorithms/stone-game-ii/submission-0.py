class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}
        n = len(piles)

        def dfs(start, turn, M):
            if start >= n:
                return 0

            if (start, turn, M) in dp:
                return dp[(start, turn, M)]

            if turn:
                curr = float('-inf')

                for end in range(start, min(start + 2 * M, n)):
                    X = end - start + 1
                    new_M = max(X, M)

                    curr = max(
                        curr,
                        sum(piles[start:end + 1])
                        + dfs(end + 1, False, new_M)
                    )

            else:
                curr = float('inf')

                for end in range(start, min(start + 2 * M, n)):
                    X = end - start + 1
                    new_M = max(X, M)

                    curr = min(
                        curr,
                        -sum(piles[start:end + 1])
                        + dfs(end + 1, True, new_M)
                    )

            dp[(start, turn, M)] = curr
            return curr

        diff = dfs(0, True, 1)
        total = sum(piles)

        return (total + diff) // 2