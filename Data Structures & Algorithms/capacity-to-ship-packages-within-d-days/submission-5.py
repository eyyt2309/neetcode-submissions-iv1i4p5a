class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        smallest = max(weights)
        highest = sum(weights)

        def calcDays(capacity):
            curr_weight = 0
            curr_days = 1

            for weight in weights:
                if curr_weight + weight <= capacity:
                    curr_weight += weight
                else:
                    curr_days += 1
                    curr_weight = weight

            return curr_days

        while smallest < highest:
            mid = (smallest + highest) // 2

            if calcDays(mid) <= days:
                highest = mid
            else:
                smallest = mid + 1

        return smallest