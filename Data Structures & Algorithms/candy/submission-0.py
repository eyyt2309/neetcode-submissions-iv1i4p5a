from collections import deque
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)

        candies = [1 for _ in range(n)]
        ans = n # starting has to have n candies as all children have at least 1 candy

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for j in range(n- 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                candies[j] = max(candies[j], candies[j + 1] + 1)
        return sum(candies)

