class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        

        rows = len(matrix)
        cols = len(matrix[0])

        x = [False for _ in range(rows)]
        y = [False for _ in range(cols)]

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    x[row] = True
                    y[col] = True

        for row in range(rows):
            for col in range(cols):
                if x[row] == True or y[col] == True:
                    matrix[row][col] = 0

        