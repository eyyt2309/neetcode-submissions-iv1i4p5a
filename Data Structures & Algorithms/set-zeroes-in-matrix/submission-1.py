class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        row_mask = 0
        col_mask = 0

        for r in range(n):
            for c in range(m):
                if matrix[r][c] == 0:
                    row_mask = row_mask | (1 << r)
                    col_mask = col_mask | (1 << c)
        for r in range(n):
            if row_mask & (1 << r):
                matrix[r] = [0] * m

        # 2. Clear marked columns
        for c in range(m):
            if col_mask & (1 << c):
                for r in range(n):
                    matrix[r][c] = 0

            
        