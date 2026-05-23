class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dfs(new_string):
            if len(new_string) == 0:
                return True
            if new_string in memo:
                return memo[new_string]

            able = False
            for i in wordDict:
                i_len = len(i)
                if new_string[0:i_len] == i:
                    able = able or dfs(new_string[i_len:])

            memo[new_string] = able
            return memo[new_string]

        return dfs(s)