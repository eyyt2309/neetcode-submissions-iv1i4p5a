class Solution:
    def countSubstrings(self, s: str) -> int:
        memo = {}

        def dfs(l, r):
            if l < 0 or r >= len(s):
                return 0

            if (l, r) in memo:
                return memo[(l, r)]

            
            if s[l] == s[r]:
                memo[(l, r)] = 1 + dfs((l - 1), (r + 1))
            else:
                return 0

            return memo[(l, r)]

        substrings = 0

        for i in range(len(s)):
            substrings += dfs(i, i)
            if i > 0:
                substrings += dfs(i - 1, i)

        return substrings