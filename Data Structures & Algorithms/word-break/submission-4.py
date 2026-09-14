class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = {}

        def dfs(curr_s):
            if curr_s == "":
                return True

            if curr_s in dp:
                return dp[curr_s]

            for word in words:
                if curr_s.startswith(word):
                    n = len(word)
                    if dfs(curr_s[n:]):
                        dp[curr_s] = True

            if curr_s not in dp:
                dp[curr_s] = False
            return dp[curr_s]

        return dfs(s)
        