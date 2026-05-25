import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        queue = deque()

        task_count = Counter(tasks)
        for task in task_count:
            heapq.heappush(heap, (-task_count[task], task))
        time = 0
        while heap or queue:
            time += 1
            print("Time: ",time)
            print("Heap: ",heap)
            print("Queue: ",queue)
            print("\n")
            if queue and queue[0][1] == time:
                (task_count, task), _ = queue.popleft()
                heapq.heappush(heap, (task_count, task))
            if heap:
                task_count, task = heapq.heappop(heap)
                task_count += 1
                if task_count < 0:
                    queue.append(((task_count, task), time + n + 1))

        return time