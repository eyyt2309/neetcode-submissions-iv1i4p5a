class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        ans = set()

        arr = []

        self.recurSum(nums, target, 0, arr, ans)

        return [list(x) for x in ans]

    def recurSum(self, nums, target, start, arr, ans):

        if target == 0:
            ans.add(tuple(arr))
            return
        elif target < 0:
            return

        for i in range(start, len(nums)):
            arr.append(nums[i])
            self.recurSum(nums, target - nums[i], i, arr, ans)
            arr.pop()
        