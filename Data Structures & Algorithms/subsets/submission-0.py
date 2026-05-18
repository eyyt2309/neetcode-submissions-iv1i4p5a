class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def dfs(nums, i, arr):
            if i == len(nums):
                self.ans.append(arr.copy())
                return

            new_arr = arr.copy()
            
            dfs(nums, i+1, new_arr)
            new_arr.append(nums[i])
            dfs(nums, i+1, new_arr)

        dfs(nums, 0, [])
        return self.ans