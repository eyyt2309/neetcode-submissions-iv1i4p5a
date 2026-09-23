from heapq import heappush, heappop
from collections import deque
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = []
        order = []
        n = len(tasks)
        
        for i, task in enumerate(tasks):
            task.append(i) # put idx for final order
        tasks.sort(key=lambda x: x[0]) # sort by enqueue time

        queue = deque(tasks)
        currentTime = queue[0][0] # start currentTime at first enqueued task

        while queue and queue[0][0] == currentTime:
            heappush(heap, (queue[0][1], queue[0][2], queue[0][0])) # sort minHeap by processingTime, idx then enqueueTime
            queue.popleft()


        while heap:
            print(heap[0])
            processingTime, idx, enqueueTime = heappop(heap)

            nextCurrentTime = currentTime + processingTime # time when cpu is free again

            order.append(idx)

            while queue and queue[0][0] <= nextCurrentTime: # when next task is enqueued before next available slot
                e, p, i = queue.popleft()
                heappush(heap, (p, i, e))
            currentTime = nextCurrentTime

            if not heap and queue: # if non-empty queue but empty heap means cpu idles, manually add the next task
                e, p ,i = queue.popleft()
                heappush(heap, (p, i, e))
                currentTime = e # set new currentTime to next enqueued task
        
        
        return order
        