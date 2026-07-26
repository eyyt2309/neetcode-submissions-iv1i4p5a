class Solution:
    def numDecodings(self, s: str) -> int:
        ch_map = {
            str(i): chr(ord("A") + i - 1) for i in range(1, 27)
        }

        dp = {}

        def dfs(s):
            if len(s) == 0:
                return 1
            if s[0] == "0":
                return 0
            if s in dp:
                return dp[s]

            ways = 0
            for digit in ch_map:
                n = len(digit)
                if digit == s[:n]:
                    ways += dfs(s[n:])
            dp[s] = ways
            return dp[s]

        return dfs(s)