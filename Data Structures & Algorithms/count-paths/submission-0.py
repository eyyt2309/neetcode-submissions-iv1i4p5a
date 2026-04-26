class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[0 for _ in range(n)] for _ in range(m)]

        for x in range(m):
            paths[x][0] = 1

        for y in range(n):
            paths[0][y] = 1


        for x in range(1, m):
            for y in range(1, n):
                paths[x][y] = paths[x-1][y] + paths[x][y-1]

        return paths[m-1][n-1]