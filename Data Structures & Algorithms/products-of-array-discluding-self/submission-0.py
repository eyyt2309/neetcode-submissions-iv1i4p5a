class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        num_length = len(nums)

        left = [None for _ in range(num_length)]
        right = [None for _ in range(num_length)]

        for i in range(num_length):
            if i == 0:
                left[i] = 1
            else:
                left[i] = left[i - 1] * nums[i - 1]

        for i in range(num_length - 1, -1, -1):
            if i == num_length - 1:
                right[i] = 1
            else:
                right[i] = right[i + 1] * nums[i + 1]

        output = [None for _ in range(num_length)]

        for i in range(num_length):
            output[i] = left[i] * right[i]

        return output