import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        
        heap = []
        buffer = []

        for i in range(n):
            heapq.heappush(heap, (-(profits[i]), capital[i])) # push (highest profit, lowest capital)

        while k > 0:
            while heap and heap[0][1] > w: # store projects that take too much capital
                buffer.append(heapq.heappop(heap))
            if heap:
                n_profits, _ = heapq.heappop(heap)
                w += abs(n_profits)
            k -=1

            while buffer:
                n_profit, capital = buffer.pop()
                heapq.heappush(heap, (n_profit, capital))

        return w
            
