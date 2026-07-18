class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l = 0
        r = n - 1

        max_area = 0

        while l < r:
            length = min(heights[l], heights[r])
            area = length * (r - l)
            max_area = max(max_area, area)

            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                l += 1

        return max_area

        