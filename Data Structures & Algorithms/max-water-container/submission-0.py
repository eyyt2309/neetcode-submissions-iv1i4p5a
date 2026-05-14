class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        for left in range(len(heights)):
            for right in range(left, len(heights)):
                area = min(heights[left], heights[right]) * (right - left)
                if area > max_area:
                    max_area = area

        return max_area
