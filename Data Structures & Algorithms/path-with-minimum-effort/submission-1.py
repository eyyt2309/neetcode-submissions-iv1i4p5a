from heapq import heappush, heappop
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n = len(heights)
        m = len(heights[0])
        heap = [[0,0,0]]

        visited = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while heap:
            diff, r, c = heappop(heap)

            if (r, c) in visited:
                continue
            
            visited.add((r, c))

            if (r, c) == (n - 1, m - 1):
                return diff

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < m:
                    newDiff = max(diff, abs(heights[r][c] - heights[nr][nc]))
                    heappush(heap, [newDiff, nr, nc])