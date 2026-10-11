from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        ans = [0 for _ in range(len(temperatures))]

        for day, temp in enumerate(temperatures):
            if not stack:
                stack.append((temp, day))
            else:
                while stack and temp > stack[-1][0]:
                    pastTemp, pastDay = stack.pop()
                    ans[pastDay] = day - pastDay
                stack.append((temp, day))
        return ans
