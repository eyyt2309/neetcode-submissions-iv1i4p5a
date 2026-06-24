class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [False for _ in range(n)]
        dp[0] = True

        reachable_count = 0

        for i in range(1, n):

            if i - minJump >= 0 and dp[i - minJump]:
                reachable_count += 1

            if i - maxJump - 1 >= 0 and dp[i - maxJump - 1]:
                reachable_count -= 1

            if s[i] == '0' and reachable_count:
                dp[i] = True

        return dp[n - 1]