class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        ans = []

        rows = len(matrix)
        cols = len(matrix[0])
        num_cells = rows * cols

        ans_len = 0
        top = 0
        bottom = rows - 1
        left = 0
        right = cols - 1

        while True:
            # left to right top row
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
                ans_len += 1
                if ans_len == num_cells:
                    return ans               
            top += 1

            # up to down right col
            for i in range(top, bottom + 1):              
                ans.append(matrix[i][right])
                ans_len += 1
                if ans_len == num_cells:
                    return ans
            right -= 1

            # right to left bottom row
            for i in range(right, left - 1, -1):              
                ans.append(matrix[bottom][i])
                ans_len += 1
                if ans_len == num_cells:
                    return ans
            bottom -= 1

            # down to up left col
            for i in range(bottom, top - 1, - 1):
                ans.append(matrix[i][left])
                ans_len += 1
                if ans_len == num_cells:
                    return ans
            left += 1


