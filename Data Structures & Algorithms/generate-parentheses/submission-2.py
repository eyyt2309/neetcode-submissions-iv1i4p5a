class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.pairs = []
        def dfs(s, left, right):
            if left + right == 2 * n:
                self.pairs.append(s)
                return

            if left < n:
                dfs(s + "(", left + 1, right)

            if right < left:
                dfs(s + ")", left, right + 1)            

        s = ""

        dfs(s, 0, 0)
        return self.pairs