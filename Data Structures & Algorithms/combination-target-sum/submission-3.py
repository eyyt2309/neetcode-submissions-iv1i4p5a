class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.ans = []
        def dfs(curr_sum, pos, arr = None):
            if pos == len(nums):
                return
            if arr == None:
                arr = []
            if curr_sum == target:
                self.ans.append(arr.copy())
                return
            elif curr_sum > target:
                return

            if curr_sum < target:
                arr.append(nums[pos])
                dfs(curr_sum + nums[pos], pos, arr)
                arr.pop()
                dfs(curr_sum, pos + 1, arr)

        dfs(0, 0)
        return self.ans