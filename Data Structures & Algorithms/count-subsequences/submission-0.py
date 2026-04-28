class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        memo = [[None for _ in range(len(t))] for _ in range(len(s))]

        self.recurString(s, t, 0 ,0, memo)

        return memo[0][0]



    def recurString(self, s, t, i, j, memo):

        # base case
        if j == len(t):
            return 1    
        if i == len(s):
            return 0

        if memo[i][j] is not None:
            return memo[i][j]

        if s[i] == t[j]:
            # if chars are equal, can either include or not include
            memo[i][j] = (self.recurString(s, t, i + 1, j + 1, memo) + self.recurString(s, t, i + 1, j, memo))
        else:
            # if chars are not equal skip to next char
            memo[i][j] = self.recurString(s, t, i + 1, j, memo)
        
        return memo[i][j]


        