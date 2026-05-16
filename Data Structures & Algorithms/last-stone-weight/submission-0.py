class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) > 1:
            stones = sorted(stones)

            if stones[-1] == stones[-2]:
                stones = stones[:-2]
            elif stones[-1] > stones[-2]:
                stones[-2] = stones[-1] - stones[-2]
                stones = stones[:-1]
        
        return stones[0] if len(stones) == 1 else 0