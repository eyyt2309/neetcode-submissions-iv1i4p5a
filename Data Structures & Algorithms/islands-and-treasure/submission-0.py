from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        queue = deque()
        seen = set()

        row_length = len(grid)
        col_length=  len(grid[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # initialize all cells adjacent to treasure and add to queue
        for rows in range(row_length):
            for cols in range(col_length):
                if grid[rows][cols] == 0:
                    if (rows,cols) not in seen:
                        queue.append((rows,cols))
                        seen.add(tuple([rows,cols]))

        # while not empty queue
        while queue:
            # pop cell from queue
            row, col = queue.popleft()
            min_list = []

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < row_length and 0 <= new_col < col_length:
                    if grid[new_row][new_col] == 2147483647:
                        grid[new_row][new_col] = min(grid[new_row][new_col], grid[row][col] + 1)
                        queue.append((new_row, new_col))
                        seen.add((new_row, new_col))