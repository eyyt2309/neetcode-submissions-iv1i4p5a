class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)

        if nums_sum % 2 == 1:
            return False

        for i in range(len(nums)):
            if self.recurSum(nums, i, 0, nums_sum // 2):
                return True
        
        return False

    def recurSum(self, nums, pos, curSum, half_sum):

        if pos > len(nums) - 1:
            return False
        if curSum == half_sum:
            return True

        return self.recurSum(nums, pos + 1, curSum + nums[pos], half_sum) or self.recurSum(nums, pos + 1, curSum, half_sum)
