import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        high = max(piles)
        low = 1
        while low <= high:
            time = 0
            mid = (high + low) // 2

            for pile in piles:
                time += math.ceil(pile / mid)
            if time > h:
                low = mid + 1
            elif time <= h:
                ans = mid
                high = mid - 1

        return ans

        

