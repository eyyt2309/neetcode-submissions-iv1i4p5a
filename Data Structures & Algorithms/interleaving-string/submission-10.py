class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}
        n = len(s3)
        s1_len = len(s1)
        s2_len = len(s2)

        if n != s1_len + s2_len:
            return False

        def dfs(i, j):
            if i + j == n:
                return True
            if (i, j) in dp:
                return dp[(i, j)]

            k = i + j

            result = False
            if i < s1_len and s3[k] == s1[i]:
                result = dfs(i + 1, j) or result
            if j < s2_len and s3[k] == s2[j]:
                result = dfs(i, j + 1) or result

            dp[(i, j)] = result
            return result

        return dfs(0,0)            