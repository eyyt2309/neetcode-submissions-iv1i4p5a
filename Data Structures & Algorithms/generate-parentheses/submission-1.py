class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dfs(s, open_count, closed_count, ans):
            if open_count == n and closed_count == n:
                ans.append(s)
                return
            
            if open_count < n:
                dfs(s+"(", open_count + 1, closed_count, ans)
            if closed_count < open_count:
                dfs(s+")", open_count, closed_count + 1, ans)                

        dfs("", 0, 0, ans)

        return ans