class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_ans = 1
        max_ans = 1
        ans = nums[0]
        for n in nums:
            tmp_min = min_ans*n
            tmp_max = max_ans*n
            max_ans = max(tmp_min, tmp_max, n)
            min_ans = min(tmp_min, tmp_max, n)
            ans = max(ans, max_ans)
        

        return ans