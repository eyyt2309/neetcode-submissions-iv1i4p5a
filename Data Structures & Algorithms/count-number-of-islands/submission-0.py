from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0

        seen = set()

        rows = len(grid)
        cols = len(grid[0])

        stack = deque()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in seen:
                    self.DFS(grid, stack, row, col, seen)
                    ans += 1

        return ans


    def DFS(self, grid, stack, row, col, seen):
        seen.add((row, col))
        print(seen)
        stack.append([row, col])

        while stack:
            node = stack.pop()
            print(node)
            seen.add((node[0], node[1]))

            if self.checkBounds(grid, node[0] - 1, node[1]) and (node[0] - 1, node[1]) not in seen:
                stack.append([node[0] - 1, node[1]])

            if self.checkBounds(grid, node[0] + 1, node[1]) and (node[0] + 1, node[1]) not in seen:
                stack.append([node[0] + 1, node[1]])

            if self.checkBounds(grid, node[0], node[1] - 1) and (node[0], node[1] - 1) not in seen:
                stack.append([node[0], node[1] - 1])

            if self.checkBounds(grid, node[0], node[1] + 1) and (node[0], node[1] + 1) not in seen:
                stack.append([node[0], node[1] + 1])
            
    def checkBounds(self, grid, row, col):
        if row < 0 or col < 0:
            return False
        
        if row >= len(grid) or col >= len(grid[0]):
            return False

        if grid[row][col] == "0":
            return False

        return True



            