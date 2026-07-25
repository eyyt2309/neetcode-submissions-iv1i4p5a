class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        def dfs(arr, nums):
            if len(arr) == n:
                ans.append(arr.copy())
                return

            for i in range(len(nums)):
                arr.append(nums[i])
                dfs(arr, nums[:i] + nums[i+1:])
                arr.pop()
        
        dfs([], nums)
        return ans

            