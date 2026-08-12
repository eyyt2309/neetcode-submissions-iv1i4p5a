class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        h = len(matrix) - 1
        n = len(matrix[0]) - 1

        while l <= h:
            mid = l + ((h - l) // 2)

            if matrix[mid][0] <= target <= matrix[mid][n]:
                left, right = 0, n
                while left <= right:
                    middle = left + ((right - left) // 2)
                    if matrix[mid][middle] == target:
                        return True
                    elif matrix[mid][middle] < target:
                        left = middle + 1
                    elif matrix[mid][middle] > target:
                        right = middle - 1
                return False

            elif target > matrix[mid][n]:
                l = mid + 1
            elif target < matrix[mid][0]:
                h = mid - 1
        return False
