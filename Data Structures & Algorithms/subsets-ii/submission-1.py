class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        nums.sort()

        def dfs(i, arr):
            result.append(arr.copy())

            for j in range(i, n):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                arr.append(nums[j])
                dfs(j + 1, arr)
                arr.pop()

        dfs(0, [])
        return result