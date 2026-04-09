import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        piles.sort()

        pile_length = len(piles)
       
        total_time = 0

        # take the largest possible k first
        max_k = piles[pile_length - 1]
        min_k = 1

        if pile_length == 1:
            return math.ceil(piles[0] / h)

        while min_k < max_k:
            mid_k = (min_k + max_k) // 2
            hour = 0
            
            for idx in range(pile_length):
                hour += math.ceil(piles[idx] / mid_k)
            # if more time taken than available time, k lies on right side 
            if hour > h:
                min_k = mid_k + 1
            # if less time or equal time taken, k lies on left side
            elif hour <= h:
                max_k = mid_k

        return min_k