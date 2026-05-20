from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        ans = [0 for _ in range(len(temperatures))]

        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append((i, temp))
            else:
                while stack and temp > stack[-1][1]:
                    idx, _ = stack.pop()
                    ans[idx] = i - idx
                stack.append((i, temp))

        return ans