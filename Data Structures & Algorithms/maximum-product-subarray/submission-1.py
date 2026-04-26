class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        ans = nums[0]
        
        product = [[0,0] for _ in range(len(nums))]

        product[0][0] = nums[0]
        product[0][1] = nums[0]

        for i, num in enumerate(nums):

            if i == 0:
                continue

            product[i][0] = max(product[i - 1][0] * nums[i], product[i - 1][1] * nums[i], nums[i])
            product[i][1] = min(product[i - 1][0] * nums[i], product[i - 1][1] * nums[i], nums[i])

            if ans < product[i][0]:
                ans = product[i][0]

        return ans