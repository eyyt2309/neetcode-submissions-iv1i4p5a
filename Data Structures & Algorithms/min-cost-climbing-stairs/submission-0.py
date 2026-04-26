class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        result = [0 for _ in range(len(cost) + 1)]

        result[0] = 0
        result[1] = 0

        for i in range(2, len(cost) + 1):
            result[i] = min(result[i - 1] + cost[i - 1], result[i - 2] + cost[i - 2])

        
        return result[len(cost)]