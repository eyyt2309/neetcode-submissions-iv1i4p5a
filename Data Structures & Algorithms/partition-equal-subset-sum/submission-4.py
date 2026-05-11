class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        memo = {}

        if nums_sum % 2 == 1:
            return False


        if self.recurSum(nums, 0, 0, nums_sum // 2, memo):
            return True
        
        return False

    def recurSum(self, nums, pos, curSum, half_sum, memo):

        if pos > len(nums) - 1:
            return False
        if curSum > half_sum:
            return False
        if curSum == half_sum:
            return True

        if (pos, curSum) in memo:
            return memo[(pos, curSum)]

        memo[(pos,curSum)] = self.recurSum(nums, pos+1, curSum+nums[pos], half_sum, memo) or self.recurSum(nums, pos+1, curSum, half_sum, memo)
        return memo[(pos,curSum)]
