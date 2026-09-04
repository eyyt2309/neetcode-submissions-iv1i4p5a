class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}

        def dfs(word1, word2):
            if len(word1) == 0:
                return len(word2)
            if len(word2) == 0:
                return len(word1)

            if (word1, word2) in dp:
                return dp[(word1, word2)]

            # if both characters in the word is the same, continue
            if word1[0] == word2[0]:
                x = dfs(word1[1:], word2[1:])
            else:
                # 3 options, insert, delete, replace
                x =  1 + min(
                    dfs(word1, word2[1:]),
                    dfs(word1[1:], word2),
                    dfs(word1[1:], word2[1:])
                )

            dp[(word1, word2)] = x
            return dp[(word1, word2)]

        return dfs(word1, word2)
        