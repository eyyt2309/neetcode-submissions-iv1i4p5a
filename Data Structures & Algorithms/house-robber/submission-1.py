class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        h = len(nums)

        def dfs(house, rob):
            if house >= h:
                return 0

            if (house, rob) in memo:
                return memo[(house, rob)]

            if rob:
                memo[(house, rob)] = max(
                    nums[house] + dfs(house + 1, False),
                    dfs(house + 1, True)
                )
            else:
                memo[(house, rob)] = dfs(house + 1, True)

            return memo[(house, rob)]

        return dfs(0, True)