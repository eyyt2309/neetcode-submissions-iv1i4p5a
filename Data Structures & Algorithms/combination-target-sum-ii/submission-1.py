class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        candidates.sort()
        def dfs(pos, curr, arr):
            if curr == target:
                ans.append(arr.copy())
                return
            if curr > target:
                return

            for i in range(pos, n):
                if i > pos and candidates[i] == candidates[i - 1]:
                    continue
                else:
                    arr.append(candidates[i])
                    dfs(i + 1, curr + candidates[i], arr)
                    arr.pop()

        arr = []
        dfs(0, 0, arr)
        return ans