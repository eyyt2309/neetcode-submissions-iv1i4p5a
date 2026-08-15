from collections import Counter
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        print(people)
        l, r = 0, len(people) - 1
        boats = 0

        while l <= r:
            if l == r:
                boats += 1
                return boats
            if people[r] == limit:
                boats += 1
                r -= 1
            elif people[l] + people[r] <= limit:
                boats += 1
                l += 1
                r -= 1
            elif people[l] + people[r] > limit and people[r] <= limit:
                boats += 1
                r -= 1
            elif people[l] + people[r] > limit and people[l] <= limit:
                boats += 1
                l += 1

        return boats