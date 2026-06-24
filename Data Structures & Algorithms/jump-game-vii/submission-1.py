class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        memo = {}

        def dfs(pos):
            if pos == len(s) - 1:
                return True
            
            if pos in memo:
                return memo[pos]

            reachable = False

            for idx in range(min(pos + maxJump, len(s) - 1), pos + minJump - 1, - 1):
                if s[idx] == '0':
                    reachable = reachable or dfs(idx)

            memo[pos] = reachable
            return memo[pos]

        return dfs(0)