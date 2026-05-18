import heapq
from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        heap = []
        fset = set(tuple(flight) for flight in flights)
        cheapest = float('inf')

        for flight in fset:
            if flight[0] == src:
                heapq.heappush(heap, (flight[2], flight[0], flight[1], 0))
        

        while heap:
            total_cost, prev, curr, stops = heapq.heappop(heap)
            # if currently at dst then update cheapest if total_cost is less than current cheapest
            if curr == dst:
                cheapest = total_cost if total_cost < cheapest else cheapest
                return cheapest if cheapest != float('inf') else -1
            
            # check for flights from current node and add them to heap
            for flight in fset:
                if flight[0] == curr and stops + 1 <= k: # if number of stops <= k then add to heap
                    heapq.heappush(heap, (flight[2] + total_cost, flight[0], flight[1], stops + 1))

        return cheapest if cheapest != float('inf') else -1



