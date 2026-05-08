from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in range(len(temperatures))]

        stack = deque()

        for idx, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][1]:
                pos, _ = stack.pop()
                result[pos] = idx - pos
            else:
                stack.append((idx, temperature))
        

        return result
