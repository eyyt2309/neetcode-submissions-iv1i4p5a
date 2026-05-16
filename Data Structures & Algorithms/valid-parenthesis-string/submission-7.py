from collections import deque

class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}
        
        def dfs(i, brace, memo):

            if brace < 0:
                return False
            
            if i == len(s):
                memo[(i, brace)] = True if brace == 0 else False

            if (i, brace) in memo:
                return memo[(i, brace)]
            
            if s[i] == '(':
                memo[(i, brace)] = dfs(i + 1, brace + 1, memo)
            elif s[i] == ')':
                memo[(i, brace)] = dfs(i + 1, brace - 1, memo)
            else:
                memo[(i, brace)] = dfs(i + 1, brace + 1, memo) or dfs(i + 1, brace - 1, memo) or dfs(i + 1, brace, memo)
            
            return memo[(i, brace)]

        dfs(0, 0, memo)

        return memo[(0, 0)]