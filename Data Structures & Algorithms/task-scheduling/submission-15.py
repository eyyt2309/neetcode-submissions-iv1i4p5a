from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task = Counter(tasks)
        cooldown = []
        heap = []
        for t in task:
            heapq.heappush(heap, (-task[t], t))

        time = 0
    
        while heap or cooldown:
            while cooldown and cooldown[0][0] == time:
                _, count, t = heapq.heappop(cooldown)
                heapq.heappush(heap, (count, t))
            if heap:
                count, t = heapq.heappop(heap)
                if count + 1 != 0:
                    heapq.heappush(cooldown, (time + n + 1, count + 1, t))
            time += 1

        return time


