class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def dfs(nums, arr):
            if len(nums) == 0:
                ans.append(arr.copy())
                return

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                arr.append(nums[i])
                dfs(nums[:i] + nums[i + 1:], arr)
                arr.pop()
    
        arr = []
        dfs(nums, arr)
        return ans