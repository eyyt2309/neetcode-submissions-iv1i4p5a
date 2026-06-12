class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def dfs(pos, arr = None):
            if arr == None:
                arr = []
            if pos == len(nums):
                self.ans.append(arr.copy())
                return


            arr.append(nums[pos])
            dfs(pos + 1, arr)
            arr.pop()
            dfs(pos + 1, arr)

        dfs(0)

        return self.ans