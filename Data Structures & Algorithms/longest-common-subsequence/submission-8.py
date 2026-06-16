class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 == text2:
            return len(text1)

        memo = {}

        def dfs(pos1, pos2):
            if pos1 == len(text1) or pos2 == len(text2):
                return 0

            if (pos1, pos2) in memo:
                return memo[(pos1, pos2)]

            if text1[pos1] == text2[pos2]:
                longest = dfs(pos1 + 1, pos2 + 1) + 1
            else:
                longest = max(dfs(pos1 + 1, pos2), dfs(pos1, pos2 + 1))
            memo[(pos1, pos2)] = longest
            return memo[(pos1, pos2)]

        return dfs(0,0)