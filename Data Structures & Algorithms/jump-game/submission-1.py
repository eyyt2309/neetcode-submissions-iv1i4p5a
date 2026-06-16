class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}

        def dfs(pos):
            if pos >= len(nums) - 1:
                return True

            if pos in memo:
                return memo[pos]

            max_jump = nums[pos]

            reach = False

            for i in range(max_jump, -1, -1):
                if i == 0:
                    continue
                else:
                    reach = reach or dfs(pos + i)

            memo[pos] = reach

            return memo[pos]

        if dfs(0):
            return True
        else:
            return False

