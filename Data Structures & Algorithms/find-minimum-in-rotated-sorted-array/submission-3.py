class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        l, r = 0, n - 1

        if len(nums) == 1:
            return nums[0]

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            elif nums[r] < nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

