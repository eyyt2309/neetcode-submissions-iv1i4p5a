class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        n = len(nums)

        def dfs(house, last, rob):
            if house >= last:
                return 0
            if (house, rob, last) in dp:
                return dp[(house, rob, last)]

            if rob:
                dp[(house, rob, last)] = max(
                    nums[house] + dfs(house + 1, last, False),
                    dfs(house + 1, last, True)
                )
            else:
                dp[(house, rob, last)] = dfs(house + 1, last, True)

            return dp[(house, rob, last)]

        return max(nums[0] + dfs(1, n - 1, False), dfs(1, n, True))