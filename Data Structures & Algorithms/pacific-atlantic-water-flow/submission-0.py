class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.pacific = False
        self.atlantic = False   
        ans = []

        def dfs(r, c, heights, visited = None):
            if self.pacific and self.atlantic:
                return 
            if r == 0 or c == 0:
                self.pacific = True

            if r == len(heights) - 1 or c == len(heights[0]) - 1:
                self.atlantic = True

            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            if visited == None:
                visited = {}
                visited[(r, c)] = True
    
            for direction in directions:
                dr, dc = direction
                nr, nc = r + dr, c + dc
                if 0 <= nr < len(heights) and 0 <= nc < len(heights[0]):
                    if heights[nr][nc] <= heights[r][c] and (nr, nc) not in visited:
                        visited[(nr, nc)] = 1
                        dfs(nr, nc, heights, visited)


        for row in range(len(heights)):
            for col in range(len(heights[0])):
                dfs(row, col, heights)
                if self.pacific and self.atlantic:
                    ans.append([row, col])
                self.atlantic = False
                self.pacific = False

        return ans