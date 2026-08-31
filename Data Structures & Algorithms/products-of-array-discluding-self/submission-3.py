class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1 for _ in range(n)]

        l_product = 1
        r_product = 1

        for i in range(n):
            output[i] = output[i] * l_product
            l_product *= nums[i]
        for j in range(n - 1, -1, -1):
            output[j] = output[j] * r_product
            r_product *= nums[j]

        return output