class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr_left = [1 for _ in range(len(nums))]
        arr_right = [1 for _ in range(len(nums))]

        for i, num in enumerate(nums):
            if i == 0:
                continue
            else:
                arr_left[i] = nums[i - 1] * arr_left[i - 1]

        for i, num in reversed(list(enumerate(nums))):
            if i == len(nums) - 1:
                continue
            else:
                arr_right[i] = nums[i + 1] * arr_right[i + 1]

        print(arr_right)

        output = [0 for _ in range(len(nums))]

        for i in range(len(nums)):
            output[i] = arr_left[i] * arr_right[i]

        return output