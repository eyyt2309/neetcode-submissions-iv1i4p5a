class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        self.ans = float('inf')     

        curr_min = nums[0]
        curr_max = nums[0]

        result = nums[0]

        for i in range(1, len(nums)):

            if nums[i] < 0:
                curr_min, curr_max = curr_max, curr_min
            curr_min = min(nums[i], nums[i] * curr_min)
            curr_max = max(nums[i], nums[i] * curr_max)

            result = max(result, curr_max)

        return result    

            

            