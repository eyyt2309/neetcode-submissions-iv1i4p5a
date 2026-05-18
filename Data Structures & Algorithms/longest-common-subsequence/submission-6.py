class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def dfs(text1, text2, i, j, memo):
            if j >= len(text2) or i >= len(text1):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]

            if text1[i] == text2[j]:
                memo[(i,j)] = dfs(text1, text2, i + 1, j + 1, memo) + 1
            else:
                memo[(i,j)] = max(dfs(text1, text2, i, j + 1, memo), dfs(text1, text2, i + 1, j, memo))

            return memo[(i,j)]

        return dfs(text1, text2, 0, 0, memo)