from collections import deque
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0 for _ in range(n)]
        right = [0 for _ in range(n)]
        area = 0
        for i in range(1, n):
            left[i] = max(height[:i])
        for j in range(n - 2, -1, - 1):
            right[j] = max(height[j:])

        for i in range(n):
            if min(left[i], right[i]) - height[i] > 0:
                area += min(left[i], right[i]) - height[i]

        return area
