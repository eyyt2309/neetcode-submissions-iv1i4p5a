class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        currSum = 0
        min_length = float('inf')
        start = 0
        for end, n in enumerate(nums):
            currSum = currSum + n
            while currSum >= target:
                min_length = min(min_length, end - start + 1)
                currSum -= nums[start]
                start += 1
        if min_length == float('inf'):
            return 0
        else:
            return min_length


