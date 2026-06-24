class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        row = len(grid)
        col = len(grid[0])

        def dfs(r,c):
            if r == 0 and c == 0:
                return grid[0][0]
            if r < 0:
                return float('inf')
            if c < 0: 
                return float('inf')

            if (r,c) in memo:
                return memo[(r,c)]

            memo[(r,c)] = grid[r][c] + min(dfs(r-1, c), dfs(r,c-1))

            return memo[(r,c)]

        return dfs(row-1,col-1)