class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        n = len(nums)
        nums.sort()

        def dfs(idx, arr):
            if idx >= n:
                ans.add(tuple(arr))
                return

            #take current idx
            arr.append(nums[idx])
            dfs(idx + 1, arr)
            arr.pop()

            #skip current idx
            dfs(idx + 1, arr)


        dfs(0, [])
        return [list(s) for s in ans]