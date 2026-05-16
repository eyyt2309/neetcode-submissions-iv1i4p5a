class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = set()
        def dfs(s, n, ans):
            if n == 0:
                ans.add(s)
                return
            
            for idx in range(len(s) + 1):
                new_string = s[:idx] + "()" + s[idx:]
                dfs(new_string, n - 1, ans)

        dfs("", n, ans)

        return list(ans)