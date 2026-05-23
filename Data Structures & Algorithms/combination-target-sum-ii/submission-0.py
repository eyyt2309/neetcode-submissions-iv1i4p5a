class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()

        def dfs(curr, arr, idx):
            if curr == target:
                ans.append(arr.copy())
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if curr + candidates[i] <= target:
                    arr.append(candidates[i])
                    dfs(curr + candidates[i], arr, i + 1)
                    arr.pop()

        dfs(0, [], 0)

        return ans
            
            