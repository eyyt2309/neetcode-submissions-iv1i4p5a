from collections import deque
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = deque()
        largestArea = 0
        heights.append(0)

        for i, height in enumerate(heights):
            if not stack or stack[-1][0] < height: # if empty stack or incoming rectangle is longer,
                stack.append((height, i))          # keep appending and extend
            else:
                start = i
                while stack and height < stack[-1][0]: # while previous rectangle is larger than incoming rectangle, calculate area now
                    prev_height, j = stack.pop() # previous height and index
                    area = prev_height * (i - j) # area = previous height * (difference in index)
                    largestArea = max(area, largestArea)
                    start = j
                stack.append((height, start))
        return largestArea
