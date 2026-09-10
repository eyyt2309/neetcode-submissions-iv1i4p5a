class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        arr = []
        wordSet = set(wordDict)
        def dfs(curr_s, remain_s):
            if remain_s == "":
                curr_s = curr_s[:-1]
                arr.append(curr_s)

            for word in wordSet:
                n = len(word)

                if remain_s[:n] == word:
                    curr_s = curr_s + word + " "
                    dfs(curr_s, remain_s[n:])
                    curr_s = curr_s[:-(n + 1)] # backtrack

        dfs("", s)
        return arr


