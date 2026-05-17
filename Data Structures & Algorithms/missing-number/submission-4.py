class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] != 0:
            return 0
        else:
            hashmap = {}
            for i, num in enumerate(nums):
                if nums[i] != i:
                    return i

        if nums[-1] != len(nums):
            return len(nums)