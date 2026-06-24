class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr_left = [1 for _ in range(n)]
        arr_right = [1 for _ in range(n)]

        for i, num in enumerate(nums):
            if i == 0:
                continue
            else:
                arr_left[i] = nums[i - 1] * arr_left[i - 1]

        for i, num in reversed(list(enumerate(nums))):
            if i == n- 1:
                continue
            else:
                arr_right[i] = nums[i + 1] * arr_right[i + 1]
        output = [0 for _ in range(len(nums))]

        for i in range(n):
            output[i] = arr_left[i] * arr_right[i]

        return output